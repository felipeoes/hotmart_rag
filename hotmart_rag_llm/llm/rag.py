import requests
from config import DB_API_HOST, DB_API_PORT, DB_API_SEARCH_ENDPOINT


class RAGDatabase:
    def __init__(self, host: str = DB_API_HOST, port: int = DB_API_PORT):
        self.__host = host
        self.__port = port
        self.__url = self.get_url()

    def get_url(self) -> str:
        return f"http://{self.__host}:{self.__port}"

    def search(self, query: str) -> list[dict]:
        """Search the database for documents related to the query.

        Input:
            - query (str): The query to search for in the database.

        Output:
            -  response (list[dict]): A list of dictionaries, where each dictionary represents a document with keys "page_content", "metadata" and "score".
        """
        response = requests.get(
            f"{self.__url}{DB_API_SEARCH_ENDPOINT}", params={"query": query}
        )
        return response.json()

