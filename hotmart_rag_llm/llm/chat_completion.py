import json
from openai import AsyncOpenAI
from typing import Union, AsyncGenerator
from config import (
    LLM_BASE_URL,
    SYSTEM_MESSAGE,
    TEMPERATURE,
    MAX_TOKENS,
    SEED,
)


class HotmartLLM:
    def __init__(self, base_url: str = LLM_BASE_URL):
        self.__client = self.get_client(base_url)

    @staticmethod
    def get_client(base_url: str) -> AsyncOpenAI:
        return AsyncOpenAI(
            base_url=base_url,
            api_key="not-needed",
        )

    async def get_chat_completion(
        self, messages: list[dict], retrieved_docs: list[dict], model: str = "llama3.2"
    ) -> dict:
        """Get the completion of a chat based on the previous messages.

        Input:
            - messages (list[dict]): list of messages exchanged in the chat.
            - retrieved_docs (list[dict]): list of retrieved documents from the vector database that are related to the user query.
            - model (str): model to be used in the completion.

        Output:
            - completion of the chat (dict).
        """
        messages = [{"role": "system", "content": SYSTEM_MESSAGE}, *messages]

        response = await self.__client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            seed=SEED,
        )

        data = {
            **response.choices[0].message.model_dump(),
            "source_docs": retrieved_docs,
        }

        return data

    async def get_chat_completion_stream(
        self,
        messages: list[dict],
        retrieved_docs: list[dict],
        model: str = "llama3.2",
    ) -> Union[str, AsyncGenerator[str, None]]:
        """Get the completion of a chat based on the previous messages.

        Input:
            - messages (list[dict]): list of messages exchanged in the chat.
            - retrieved_docs (list[dict]): list of retrieved documents from the vector database that are related to the user query.
            - model (str): model to be used in the completion.


        Output:
            - generator of completions of the chat (str).
        """
        messages = [{"role": "system", "content": SYSTEM_MESSAGE}, *messages]

        stream = await self.__client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            seed=SEED,
            stream=True,
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0], end="")
                # format to be an event-stream
                data = {
                    "content": chunk.choices[0].delta.content,
                    "finish_reason": chunk.choices[0].finish_reason,
                }
                yield f"data: {json.dumps(data)}\n\n"

            # final chunk, add information about retrieved documents
            print(chunk.choices[0].finish_reason)
            if chunk.choices[0].finish_reason is not None:
                data = {
                    "content": "",
                    "finish_reason": chunk.choices[0].finish_reason,
                    "source_docs": retrieved_docs,
                }
                yield f"data: {json.dumps(data)}\n\n"
