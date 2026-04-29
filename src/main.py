# src/main.py
import sys
from pathlib import Path
from app import PersonalLibraryApp  # Import the main app class
import tkinter as tk


def main():
    """Entry point for the Personal Library App."""
    print("Personal Library App (Alpha)")
    print(f"Running on: {sys.platform}")

    # Cross-platform data directory
    data_dir = Path.home() / "PersonalLibraryApp"
    data_dir.mkdir(exist_ok=True)
    print(f"Data will be stored in: {data_dir}")

    # Initialize and run the GUI
    root = tk.Tk()
    app = PersonalLibraryApp(root, 'PersonalLibraryApp', 'stevenmichaelpotter@yahoo.com')
    root.mainloop()

if __name__ == "__main__":
    main()