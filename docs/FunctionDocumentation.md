# Function Documentation for Personal Library App

## Database Class in `database.py`

### Overview  
The `Database` class handles all interactions with the SQLite database, including creating tables and adding book entries to the personal library. 

### Methods  

#### `__init__(self, db_name: str = 'library.db')`
- **Purpose**: Initializes the database connection and creates the books table if it doesn’t already exist. 
- **Parameters**: 
  - `db_name`: Name of the SQLite database file (default is 'library.db').  

#### `create_books_table(self) -> None`
- **Purpose**: Creates the `books` table with the necessary fields to store book information.  
- **Fields**:  
  - `id`: Primary key, auto-incremented.  
  - `title`: Title of the book (text).  
  - `isbn`: Unique identifier for the book (text).  
  - `author_first`: First name of the author (text).  
  - `author_last`: Last name of the author (text).  
  - `genre`: Genre of the book (text).  
  - `format`: Format type (e.g., hardcover, paperback) (text).  
  - `cover_image`: URL of the cover image thumbnail (text).  
  - `user_notes`: Optional notes about the book, with a 200-character limit (text).  

#### `add_book(self, title: str, isbn: str, author_first: str = '', author_last: str = '', genre: str = '', format_type: str = '', cover_image: str = '', user_notes: str = '') -> None`
- **Purpose**: Inserts a new book entry into the `books` table.  
- **Parameters**: All the parameters correspond to the fields in the `books` table, allowing for flexible entry of book details.  

#### `close(self) -> None`
- **Purpose**: Closes the database connection. 

---

## OpenLibraryAPI Class in `api.py`

### Overview  
The `OpenLibraryAPI` class facilitates interaction with the Open Library API for searching books by ISBN or title. 

### Methods 

#### `__init__(self, user_agent: str, email: str) -> None`
- **Purpose**: Initializes the API class with headers for making requests.  
- **Parameters**:  
  - `user_agent`: The name of the application making the request.  
  - `email`: Contact email for rate limit notifications.  

#### `search_by_isbn(self, isbn: str) -> dict`
- **Purpose**: Searches for a book using its ISBN through the Open Library API.  
- **Parameters**:  
  - `isbn`: The ISBN number of the book.  
- **Return**: A dictionary containing the search results or an error message.  

#### `search_by_title(self, title: str) -> dict`
- **Purpose**: Searches for a book using its title through the Open Library API.  
- **Parameters**:  
  - `title`: The title of the book.  
- **Return**: A dictionary containing the search results or an error message.  

#### `_handle_response(self, response: requests.Response) -> dict`
- **Purpose**: Handles and checks the API response. If successful, it returns the parsed JSON; otherwise, it returns an error message.  
- **Parameters**:  
  - `response`: The response object from the requests library.  
- **Return**: Parsed JSON or error details.  

---

## PersonalLibraryApp Class in `app.py`

### Overview  
The `PersonalLibraryApp` class manages the user interface, allowing users to interact with the application. It integrates the database and API functionality into a Tkinter GUI.  

### Methods  

#### `__init__(self, root: tk.Tk, user_agent: str, email: str) -> None`
- **Purpose**: Initializes the main application and TKinter window setup.  
- **Parameters**:  
  - `root`: The main Tkinter window instance.  
  - `user_agent`: User agent string for API requests.  
  - `email`: Contact email for API requests.  

#### `create_widgets(self) -> None`
- **Purpose**: Creates and places the GUI components (labels, entry fields, buttons, and text area).  

#### `search_books(self) -> None`
- **Purpose**: Retrieves user input, validates it, and initiates a search for books using the Open Library API.  
- **Return**: Displays results or error notifications based on user input.  

#### `display_search_results(self, results: dict) -> None`
- **Purpose**: Displays the search results in the text area. If there's an error, it shows an error message.  
- **Parameters**:  
  - `results`: The dictionary containing the API response.  

---

This documentation outlines the functionality and purpose of the various components within the Personal Library App. Each method is designed to fulfill specific tasks, ensuring the application operates smoothly and efficiently.