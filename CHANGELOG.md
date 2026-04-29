# Changelog for Personal Library App

## [Unreleased]

### April 22, 2026
#### Added
- Implemented the ability to search for books by ISBN and title using the Open Library API.
- Formatted search results for better readability in the GUI output.
- Added functionality to trigger the search action by pressing the Enter key in the input field.
#### Changed
- Updated the API endpoint used for searching by title to the correct URL schema based on Open Library API requirements.
- Enhanced the GUI layout allowing the results section to resize along with the main application window.
#### Fixed
- Resolved return type issues in the OpenLibraryAPI class to ensure consistent response types from API calls.

## April 27, 2026
#### Added
- Three separate input fields for Title, Author, and ISBN for more precise searching.
- A checkbox labeled 'Match All Fields' to refine search criteria based on filled fields.
- Dialog functionality to add selected books to either Owned library or Wishlist with optional user notes.
#### Changed
- Adjusted the UI layout for better user experience and responsiveness, ensuring labels align to the left.
- Refined search logic to allow partial matches irrespective of checkbox state when performing API queries.
#### Fixed
- Resolved issues with Enter key functionality for initiating searches across all fields.
- Addressed issues with search results only returning exact matches when the 'Match All Fields' checkbox was unchecked.
