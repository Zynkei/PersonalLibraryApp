import requests

class OpenLibraryAPI:
    """
    A class to interact with the Open Library API for book searches.
    """

    BASE_URL = 'https://openlibrary.org/api/books'

    def __init__(self, user_agent: str, email: str) -> None:
        """
        Initialize the OpenLibraryAPI class with user agent and contact info.
        :param user_agent: Name of the application
        :param email: Contact email for notifications
        """
        self.headers = {'User-Agent': f'{user_agent} ({email})'}

    def search_by_isbn(self, isbn: str) -> dict:
        """
        Search for a book by its ISBN using the Open Library API.
        :param isbn: The ISBN of the book to search
        :return: JSON response from the API
        """
        response = requests.get(f'{self.BASE_URL}?bibkeys=ISBN:{isbn}&format=json', headers=self.headers)
        return self._handle_response(response)

    def search_by_title(self, title: str) -> dict:
        """
        Search for a book by its title using the Open Library API.
        :param title: The title of the book to search
        :return: JSON response from the API
        """
        response = requests.get(f'https://openlibrary.org/search.json?title={title}', headers=self.headers)
        return self._handle_response(response)  # Return the processed result

    def _handle_response(self, response: requests.Response) -> dict:
        """
        Handle the API response and check for errors.
        :param response: The response object from the requests library
        :return: Parsed JSON if successful, or an error dictionary
        """
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.status_code, 'message': response.text}