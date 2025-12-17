# Music Playlist System

A console-based music playlist management system built in Python. Users can authenticate, manage playlists, add/edit/remove songs, sort, shuffle, and export data.

## Features

- **Authentication**: Secure login with username and password.
- **Playlist Management**:
  - Add songs to playlists (with name, singer, genre).
  - Change song details in playlists.
  - Rename playlists.
  - Remove playlists (including all songs).
  - Remove specific songs from playlists.
- **Analysis**:
  - Identify duplicated songs across playlists.
- **Sorting & Shuffling**:
  - Sort playlists by name (ascending).
  - Sort songs in each playlist by name (ascending).
  - Shuffle songs in a playlist.
- **Data Persistence**:
  - Import playlists from JSON files.
  - Export playlists to a human-readable text file.
- **Console Interface**: Simple menu-driven interface for all operations.

## Requirements

- Python 3.x
- No external dependencies (uses built-in `json` and `random`).

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/jrmwaro/music_play_systems.git
   cd music_play_systems
   ```

2. Ensure Python is installed (run `python --version`).

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Log in with the credentials:
   - Username: `user123`
   - Password: `Givemetheykey123`

3. Use the menu to perform operations (1-12).

### Menu Options

1. Add song to a playlist
2. Change song in a playlist
3. Rename a playlist
4. Remove a playlist
5. Remove a song from a playlist
6. Identify duplicated songs
7. Sort playlists by name
8. Sort songs in each playlist
9. Shuffle songs in a playlist
10. Export playlists to file
11. Import playlists from file
12. Display all playlists and songs
13. Exit

## Data Files

- `data/playlists.txt`: JSON file for storing playlists (auto-loaded on start, saved on exit).
- `data/exported_playlists.txt`: Human-readable export file.

## Project Structure

- `main.py`: Main application logic and menu.
- `auth.py`: User authentication.
- `data/playlist.py`: Song and Playlist classes.
- `data/playlists.txt`: Playlist data storage.
- Other files: Utilities and tests.

## Contributing

Feel free to fork, submit issues, or pull requests!

## License

This project is open-source. Use at your own risk.