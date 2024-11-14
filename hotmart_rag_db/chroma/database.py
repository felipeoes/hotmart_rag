import chromadb
from chromadb.config import Settings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# from langchain_community.embeddings.sentence_transformer import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import *


class ChromaDB:
    """Class to interact with the Chroma database.

    Attributes:
        - host (str): The host of the Chroma database.
        - port (int): The port on which the Chroma database service is listening.
        - collection_name (str): The name of the collection in the Chroma database.
        - embedding_model (str): The name of the embedding model.
        - embedding_function (HuggingFaceEmbeddings): The embedding function that will be used to convert text to embeddings.
    """

    def __init__(
        self, host: str, port: int, collection_name: str, embedding_model: str
    ):
        self.host = host
        self.port = port
        self.collection_name = collection_name
        self.embedding_model = embedding_model
        self.embedding_function = HuggingFaceEmbeddings(
            model_name=self.embedding_model, model_kwargs={"trust_remote_code": True}
        )
        self.client = self.__initialize_client__()
        self.chroma = Chroma(
            client=self.client,
            collection_name=self.collection_name,
            embedding_function=self.embedding_function,
        )

    def __initialize_client__(self):
        """Initialize the Chroma client."""
        return chromadb.HttpClient(
            host=self.host,
            port=self.port,
            settings=Settings(
                chroma_client_auth_provider="chromadb.auth.basic_authn.BasicAuthClientProvider",
                chroma_client_auth_credentials=CHROMA_CLIENT_AUTH_CREDENTIALS,
            ),
        )

    def _preprocess_documents(self, documents: list[Document]) -> list[Document]:
        """Preprocess documents by splitting them into chunks of `CHUNK_SIZE` characters, having an overlap of `CHUNK_OVERLAP` characters.

        Input:
            - documents (list[Document]): A list of documents to preprocess.

        Output:
            - chunked_docs (list[Document]): A list of documents where each document has been split into chunks.

        """
        # split text into paragraphs
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        )

        chunked_docs = text_splitter.split_documents(
            [Document(page_content=doc.page_content, metadata={}) for doc in documents]
        )
        return chunked_docs

    def add_documents(self, documents: list[Document]) -> list[str]:
        """Add documents to the Chroma database (already processed and transformed into embeddings).

        Input:
            - documents (list[Document]): A list of documents to add to the database.

        Output:
            - document_ids (list[str]): A list of document IDs that were added to the database.
        """
        # preprocess documents
        documents = self._preprocess_documents(documents)

        # add documents to the database
        return self.chroma.add_documents(documents)

    def search(self, query: str, num_results: int = 2):
        """Search the Chroma database and format the output to be a list of dicts, including the document content and the similarity score.

        Input:
            - query (str): The query to search for in the database.
            - num_results (int): The number of results to return.

        Output:
            - results (list[dict]): A list of dictionaries, where each dictionary has the keys "content" and "distance".
        """
        doc_scores = self.chroma.similarity_search_with_score(query, num_results)
        results: list[dict] = [
            {"content": doc.page_content, "metadata": doc.metadata, "distance": distance}
            for doc, distance in doc_scores
        ]

        return results
        # return self.chroma.similarity_search_with_score(query, num_results)


chroma_db = ChromaDB(
    host=CHROMA_HOST,
    port=CHROMA_PORT,
    collection_name=CHROMA_COLLECTION_NAME,
    embedding_model=CHROMA_EMBEDDING_MODEL,
)
