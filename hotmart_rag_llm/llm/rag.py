import requests
from config import DB_API_HOST, DB_API_PORT, DB_API_SEARCH_ENDPOINT


class RAGDatabase:
    """Class to interact with the RAG database microservice.

    Attributes:
        - host (str): The host of the database microservice.
        - port (int): The port of the database microservice.
        - url (str): The URL of the database microservice.
    """

    def __init__(self, host: str = DB_API_HOST, port: int = DB_API_PORT):
        self.__host = host.strip()
        self.__port = port
        self.__url = self.get_url()

    def get_url(self) -> str:
        """Get the URL of the database microservice.

        Output:
            - url (str): The URL of the database microservice.
        """

        # check if protocol is already in the host
        if "http://" in self.__host or "https://" in self.__host:
            return f"{self.__host}:{self.__port}"

        return f"http://{self.__host}:{self.__port}"

    def search(self, query: str) -> list[dict]:
        """Search the database for documents related to the query.

        Input:
            - query (str): The query to search for in the database.

        Output:
            -  response (list[dict]): A list of dictionaries, where each dictionary represents a document with keys "page_content", "metadata" and "score".
        """

        try:
            search_url = f"{self.__url}/{DB_API_SEARCH_ENDPOINT}"
            response = requests.get(
                search_url,
                params={"query": query},
            )

            return response.json()

        except Exception as e:
            print(f"Error querying the database: {e}")
            return []
