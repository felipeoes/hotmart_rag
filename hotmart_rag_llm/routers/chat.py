from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from llm.rag import RAGDatabase
from llm.chat_completion import HotmartLLM
from pydantic import BaseModel

router = APIRouter(
    responses={404: {"description": "Not found"}},
)

hotmart_llm = HotmartLLM()
rag_db = RAGDatabase()


class QueryRequest(BaseModel):
    query: str
    stream: bool = True


def format_user_prompt(query: str, retrieved_docs: list[dict]) -> str:
    """Format the user prompt to be fed into the LLM model.

    Input:
        - query (str): The user query.
        - retrieved_docs (list[dict]): A list of dictionaries, where each dictionary represents a document with keys "content", "metadata" and "distance".

    Output:
        - formatted_prompt (str): The formatted user prompt.
    """

    formatted_prompt = ""
    for i, doc in enumerate(retrieved_docs):
        formatted_prompt += f"### DOCUMENTO {i+1}: {doc['content']}\n\n"

    formatted_prompt += f"### PERGUNTA: {query}\n\n"

    return formatted_prompt


@router.post("/chat")
async def chat(query_req: QueryRequest):
    # call the rag database microservice to get the documents
    retrieved_docs = rag_db.search(query_req.query)

    # format the user prompt and get the chat completion
    user_prompt = format_user_prompt(query_req.query, retrieved_docs)
    messages = [{"role": "user", "content": user_prompt}]

    print(messages)

    if query_req.stream:
        return StreamingResponse(
            hotmart_llm.get_chat_completion_stream(messages, retrieved_docs),
            media_type="text/event-stream",
        )

    return await hotmart_llm.get_chat_completion(messages, retrieved_docs)
