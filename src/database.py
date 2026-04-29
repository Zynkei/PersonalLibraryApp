import os
import sqlite3

class Database:
    """
    A class to interact with the SQLite database for storing personal library information.
    """

    def __init__(self, db_name: str = 'library.db') -> None:
        """
        Initialize the Database class and create the database if it doesn't exist.
        :param db_name: Name of the database file
        """
        # Get the directory where this file (database.py) is located
        dir_path = os.path.dirname(os.path.abspath(__file__))
        # Create the full path for the database file
        db_path = os.path.join(dir_path, db_name)
        
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self) -> None:
        """
        Create tables for storing books, owned books, and wishlist books if they don't already exist.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            olid TEXT UNIQUE,
            -- Allow NULL for olid to support edge cases
            CHECK (length(olid) = 0 OR olid IS NOT NULL)
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Owned (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            notes TEXT,
            FOREIGN KEY (book_id) REFERENCES Books (id)
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Wishlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            notes TEXT,
            FOREIGN KEY (book_id) REFERENCES Books (id)
        )
        ''')
        self.connection.commit()

    def add_book(self, title: str, isbn: str, author_first: str = '', author_last: str = '',
                 genre: str = '', format_type: str = '', cover_image: str = '',
                 user_notes: str = '') -> None:
        """
        Add a new book entry to the database.
        :param title: Title of the book
        :param isbn: ISBN of the book
        :param author_first: First name of the author
        :param author_last: Last name of the author
        :param genre: Genre of the book
        :param format_type: Format of the book (e.g., 'hardcover', 'paperback')
        :param cover_image: URL of the cover image thumbnail
        :param user_notes: User notes about the book
        """
        self.cursor.execute('''
        INSERT INTO books (title, isbn, author_first, author_last, genre, format, cover_image, user_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (title, isbn, author_first, author_last, genre, format_type, cover_image, user_notes))
        self.connection.commit()

    def add_to_owned(self, book_id: str, notes: str = '') -> None:
        """
        Logic to add the book to the Owned table in the database.
        :param book_id: The id of the selected book
        :param notes: User notes for the book entry
        """
        self.cursor.execute('''
        INSERT INTO Owned (book_id, notes)
        VALUES (?, ?)''', (book_id, notes))
        self.connection.commit()

    def add_to_wishlist(self, book_id: str, notes: str = '') -> None:
        """
        Logic to add the book to the Wishlist table in the database.
        :param book_id: The id of the selected book
        :param notes: User notes for the book entry
        """
        self.cursor.execute('''
        INSERT INTO Wishlist (book_id, notes)
        VALUES (?, ?)''', (book_id, notes))
        self.connection.commit()

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.connection.close()

