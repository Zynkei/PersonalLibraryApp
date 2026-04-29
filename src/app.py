import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from database import Database
from api import OpenLibraryAPI
import requests

class PersonalLibraryApp:
    """
    Main application class for the Personal Library App.
    It handles user interactions and API requests.
    """



    def __init__(self, root: tk.Tk, user_agent: str, email: str) -> None:
        """
        Initialize the application and set up the GUI.
        :param root: The main Tkinter window
        :param user_agent: User agent string for API requests
        :param email: Contact email for API requests
        """
        self.root = root
        self.root.title('Personal Library App')
        self.api = OpenLibraryAPI(user_agent, email)
        self.db = Database()
        self.sort_state: dict[str, str | None] = {'Title': None, 'Author': None, 'First Published': None}
        self.original_data = []  # Initialize with an empty list
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Create and place GUI widgets.
        """
        tk.Label(self.root, text='Enter Title:').grid(row=0, column=0, sticky='w')  # Align left
        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.grid(row=0, column=1)
        self.title_entry.bind('<Return>', lambda event: self.search_books())  # Bind the Enter key to title

        tk.Label(self.root, text='Enter Author:').grid(row=1, column=0, sticky='w')  # Align left
        self.author_entry = tk.Entry(self.root, width=50)
        self.author_entry.grid(row=1, column=1)
        self.author_entry.bind('<Return>', lambda event: self.search_books())  # Bind the Enter key to author

        tk.Label(self.root, text='Enter ISBN:').grid(row=2, column=0, sticky='w')  # Align left
        self.isbn_entry = tk.Entry(self.root, width=50)
        self.isbn_entry.grid(row=2, column=1)
        self.isbn_entry.bind('<Return>', lambda event: self.search_books())  # Bind the Enter key to ISBN

        self.match_all_var = tk.BooleanVar()
        self.match_all_checkbox = tk.Checkbutton(self.root, text='Match All Fields', variable=self.match_all_var)
        self.match_all_checkbox.grid(row=3, columnspan=2)

        tk.Button(self.root, text='Search', command=self.search_books).grid(row=4, columnspan=2)

        # Create a Treeview for displaying results
        self.results_tree = ttk.Treeview(self.root, columns=('Title', 'Author', 'First Published'), show='headings')
        self.results_tree.heading('Title', text='Title', command=lambda: self.sort_tree('Title'))
        self.results_tree.heading('Author', text='Author', command=lambda: self.sort_tree('Author'))
        self.results_tree.heading('First Published', text='First Published', command=lambda: self.sort_tree('First Published'))
        self.results_tree.grid(row=5, column=0, columnspan=2, sticky='nsew')

        self.root.grid_rowconfigure(5, weight=1)  # Allow the results tree view to expand
        self.root.grid_columnconfigure(1, weight=1)  

    def search_books(self) -> None:
        """
        Get the user's input and search for books using the Open Library API.
        """
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        isbn = self.isbn_entry.get().strip()

        if not title and not author and not isbn:
            messagebox.showwarning('Warning', 'Please enter at least one search field (Title, Author, or ISBN).')
            return

        # Construct the API request based on the input fields
        query_params = []

        if title:
            query_params.append(f'title={title}')
        if author:
            query_params.append(f'author={author}')
        if isbn:
            query_params.append(f'bibkeys=ISBN:{isbn}')

        # Update the API call based on the checkbox state
        base_url = 'https://openlibrary.org/search.json?'
        if self.match_all_var.get():
            # Adding combined search logic (AND matching)
            api_url = base_url + '&'.join(query_params)
        else:
            api_url = base_url + '&'.join(query_params)

        response = requests.get(api_url)
        results = self.api._handle_response(response)

        self.display_search_results(results)

    def display_search_results(self, results: dict) -> None:
        """
        Display the search results in the tree view.
        :param results: The results obtained from the API
        """
        for row in self.results_tree.get_children():  # Clear previous results
            self.results_tree.delete(row)
        if 'error' in results:
            messagebox.showerror('Error', f'Error {results["error"]}: {results["message"]}')
            return

        # Store original order of results
        self.original_data = []  # Clear existing original data
        for book in results.get('docs', []):
            title = book.get('title', 'No Title')
            authors = ', '.join(book.get('author_name', []))
            first_publish_year = book.get('first_publish_year', 'Unknown Year')
            self.results_tree.insert('', 'end', values=(title, authors, first_publish_year))
            self.original_data.append((title, authors, first_publish_year))  # Store original data for restoring order

#    def sort_tree(self, column: str) -> None:
#        """
#        Sort the Treeview by the selected column.
#        :param column: The column to sort by
#        """
#        # Retrieve current entries from the Treeview
#        data = [(self.results_tree.item(item)['values'], item) for item in self.results_tree.get_children()]

        # Determine sort index
#        column_index = {'Title': 0, 'Author': 1, 'First Published': 2}[column]

        # Toggle sorting order
#        if self.sort_state[column] == 'ascending':

    def sort_tree(self, column: str) -> None:
        """Sort Treeview by column (toggle: ascending -> descending -> original)."""
        col_index = {'Title': 0, 'Author': 1, 'First Published': 2}[column]
        
        # Get current data from the tree
        items = [(self.results_tree.item(item)['values'], item) for item in self.results_tree.get_children()]
        
        # Determine next sort state
        current = self.sort_state.get(column)
        if current is None:
            next_state = 'ascending'
        elif current == 'ascending':
            next_state = 'descending'
        else:  # descending
            next_state = None   # go back to original order
        
        self.sort_state[column] = next_state
        
        # Apply sorting or restore original order
        if next_state == 'ascending':
            items.sort(key=lambda x: x[0][col_index])
        elif next_state == 'descending':
            items.sort(key=lambda x: x[0][col_index], reverse=True)
        else:   # restore original order
            items = [(values, None) for values in self.original_data]   # rebuild from stored original data
        
        # Clear and repopulate the tree
        self.results_tree.delete(*self.results_tree.get_children())
        for values, _ in items:
            self.results_tree.insert('', 'end', values=tuple(values))   # ← fixed

    def on_result_click(self, event) -> None:
        selected = self.results_tree.selection()
        if not selected:
            return
        values = self.results_tree.item(selected[0], 'values')
        title, authors = values[0], values[1]
        if messagebox.askyesno('Add to Library', f'Add "{title}" by {authors}?'):
            self.add_book_dialog(title)   # Note: you must pass a book ID, not just title – see fix below

    def add_book_dialog(self, book_id: str) -> None:
        """
        Show a dialog to add the selected book to Owned or Wishlist.
        """
        dialog = tk.Toplevel(self.root)
        dialog.title('Add Book')

        tk.Label(dialog, text='Enter Notes (optional):').grid(row=0, column=0)
        notes_entry = tk.Entry(dialog, width=50)
        notes_entry.grid(row=0, column=1)
        tk.Button(dialog, text='Add to Owned', command=lambda: self.add_to_owned(book_id, notes_entry.get())).grid(row=1, column=0)
        tk.Button(dialog, text='Add to Wishlist', command=lambda: self.add_to_wishlist(book_id, notes_entry.get())).grid(row=1, column=1)
    def add_to_owned(self, book_id: str, notes: str) -> None:
        """
        Logic to add the book to the Owned table in the database.
        :param book_id: The id of the selected book
        :param notes: User notes for the book entry
        """
        self.db.add_to_owned(book_id, notes)  # Call the database method
        messagebox.showinfo('Success', 'Book added to Owned!')
    def add_to_wishlist(self, book_id: str, notes: str) -> None:
        """
        Logic to add the book to the Wishlist table in the database.
        :param book_id: The id of the selected book
        :param notes: User notes for the book entry
        """
        self.db.add_to_wishlist(book_id, notes)  # Call the database method
        messagebox.showinfo('Success', 'Book added to Wishlist!')
if __name__ == '__main__':
    root = tk.Tk()
    app = PersonalLibraryApp(root, 'MyLibraryApp', 'contact@example.org')
    root.mainloop()