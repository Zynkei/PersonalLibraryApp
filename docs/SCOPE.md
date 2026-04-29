# Personal Library App - Scope Statement

## Project Overview  
A personal inventory system for physical books, with future expansion to other media types.  
- **Alpha Goal**: Local-only app with manual ISBN/title search.  
- **0.1 Goal**: Initial functionality for searching and adding books to the user's library.
- **1.0 Goal**: Barcode scanning + cloud sync.  

## Versioning
- **0.x**: Pre-release versions reflecting incremental updates and features.
- **1.0**: First production-ready release with basic functionality.

## Features  
### 0.1 Version
- Search books by ISBN/title using [Open Library API] (identified requests: 180 reqs/min).  
- Display matches and select the correct book to add to their personal library.
- Store library data in a local SQLite database with the following attributes:
  - Title
  - ISBN
  - Author (first and last if available)
  - Genre (if available)
  - Format (hardcover, paperback, etc. if available)
  - Cover image thumbnail
  - User notes (200 character limit, optional)
- Notify the user if a matching book already exists in their library and offer options to view or add another copy before proceeding with API calls.
- View and manage the current library, with options to modify and delete entries.

### 1.0 Version  
- Barcode scanning for ISBN lookup.  
- Cloud storage integration (e.g., Dropbox/Google Drive API).  
- Export/import functionality for backups.  

## Technical Constraints  
- **Open Library API**: Requires `User-Agent` header for higher rate limits (3 reqs/sec).  
- **Local Storage**: SQLite for scalability and future cloud migration.  
- **Error Handling**:
  - API calls will be throttled to avoid exceeding limits.
  - If 90% of the API call limit is approached, a notification will alert the user.
  - If the rate limit is reached, the user will see a countdown until the next available call.
- **Cross-Platform GUI**: Designed for mobile and desktop compatibility, ensuring ease of use for non-technical users.
## Out of Scope  
- User authentication (initially).  
- Mobile app development (desktop-first).  

## Future Compatibility  
- SQLite schema designed for cloud migration.  
- Abstracted API calls for easy service swaps.  
- UI logic separated for mobile/desktop adaptations.