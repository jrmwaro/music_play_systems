from auth import authenticate_user
from data.playlist import Playlist, Song
import random
import json


def show_menu():
    """Displays the main menu options."""
    print("\n====== Music Playlist System Menu ======")
    print("1. Add song to a playlist")
    print("2. Change song in a playlist")
    print("3. Rename a playlist")
    print("4. Remove a playlist")
    print("5. Remove a song from a playlist")
    print("6. Identify duplicated songs")
    print("7. Sort playlists by name")
    print("8. Sort songs in each playlist")
    print("9. Shuffle songs in a playlist")
    print("10. Export playlists to file")
    print("11. Import playlists from file")
    print("12. Display all playlists and songs")
    print("13. Exit")
    print("========================================")


def load_playlists():
    """Loads playlists from file if exists."""
    try:
        with open('data/playlists.txt', 'r') as f:
            data = json.load(f)
            playlists = []
            for p_data in data:
                playlist = Playlist(p_data['name'])
                for s_data in p_data['songs']:
                    song = Song(s_data['name'], s_data['singer'], s_data['genre'])
                    playlist.add_song(song)
                playlists.append(playlist)
            return playlists
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_playlists(playlists):
    """Saves playlists to file."""
    data = []
    for p in playlists:
        p_data = {'name': p.name, 'songs': [{'name': s.name, 'singer': s.singer, 'genre': s.genre} for s in p.songs]}
        data.append(p_data)
    with open('data/playlists.txt', 'w') as f:
        json.dump(data, f, indent=4)


def find_playlist(playlists, name):
    """Finds a playlist by name."""
    for p in playlists:
        if p.name.lower() == name.lower():
            return p
    return None


def main(): 
    
    
    print("Welcome to the Music Playlist System")

    if not authenticate_user():
        print("Access denied.")
        return

    playlists = load_playlists()

    while True:
        show_menu()
        choice = input("Choose an option (1-13): ")

        if choice == "1":
            # Add song to playlist
            name = input("Enter playlist name: ")
            playlist = find_playlist(playlists, name)
            if not playlist:
                playlist = Playlist(name)
                playlists.append(playlist)
            song_name = input("Enter song name: ")
            singer = input("Enter singer: ")
            genre = input("Enter genre: ")
            song = Song(song_name, singer, genre)
            playlist.add_song(song)
            print(f"Added {song} to {playlist.name}")
        elif choice == "2":
            # Change song in playlist
            name = input("Enter playlist name: ")
            playlist = find_playlist(playlists, name)
            if not playlist:
                print("Playlist not found.")
                continue
            old_name = input("Enter song name to change: ")
            if not playlist.has_song(old_name):
                print("Song not found in playlist.")
                continue
            new_name = input("Enter new song name: ")
            singer = input("Enter new singer: ")
            genre = input("Enter new genre: ")
            playlist.remove_song(old_name)
            song = Song(new_name, singer, genre)
            playlist.add_song(song)
            print(f"Changed song to {song} in {playlist.name}")
        elif choice == "3":
            # Rename playlist
            name = input("Enter current playlist name: ")
            playlist = find_playlist(playlists, name)
            if not playlist:
                print("Playlist not found.")
                continue
            new_name = input("Enter new playlist name: ")
            playlist.rename(new_name)
            print(f"Renamed playlist to {new_name}")
        elif choice == "4":
            # Remove playlist
            name = input("Enter playlist name to remove: ")
            playlist = find_playlist(playlists, name)
            if not playlist:
                print("Playlist not found.")
                continue
            playlists.remove(playlist)
            print(f"Removed playlist {name}")
        elif choice == "5":
            # Remove song from playlist
            name = input("Enter playlist name: ")
            playlist = find_playlist(playlists, name)
            if not playlist:
                print("Playlist not found.")
                continue
            song_name = input("Enter song name to remove: ")
            if playlist.remove_song(song_name):
                print(f"Removed {song_name} from {playlist.name}")
            else:
                print("Song not found.")
        elif choice == "6":
            # Identify duplicated songs
            all_songs = {}
            for p in playlists:
                for s in p.songs:
                    key = (s.name.lower(), s.singer.lower())
                    if key in all_songs:
                        all_songs[key].append(p.name)
                    else:
                        all_songs[key] = [p.name]
            duplicates = {k: v for k, v in all_songs.items() if len(v) > 1}
            if duplicates:
                print("Duplicated songs:")
                for (name, singer), pls in duplicates.items():
                    print(f"{name} by {singer} in playlists: {', '.join(pls)}")
            else:
                print("No duplicated songs found.")
        elif choice == "7":
            # Sort playlists by name
            playlists.sort(key=lambda p: p.name.lower())
            print("Playlists sorted by name.")
        elif choice == "8":
            # Sort songs in each playlist
            for p in playlists:
                p.songs.sort(key=lambda s: s.name.lower())
            print("Songs sorted in each playlist.")
        elif choice == "9":
            # Shuffle songs in a playlist
            name = input("Enter playlist name: ")
            playlist = find_playlist(playlists, name)
            if not playlist:
                print("Playlist not found.")
                continue
            random.shuffle(playlist.songs)
            print(f"Shuffled songs in {playlist.name}")
        elif choice == "10":
            # Export playlists to file
            with open('data/exported_playlists.txt', 'w') as f:
                for p in playlists:
                    if p.songs:
                        song_list = ", ".join(str(song) for song in p.songs)
                        f.write(f"{p.name}: {song_list}\n")
                    else:
                        f.write(f"{p.name}: (No songs)\n")
            print("Playlists exported to data/exported_playlists.txt")
        elif choice == "11":
            # Import playlists from file
            filename = input("Enter the filename to import from (e.g., data/playlists.txt): ")
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    for p_data in data:
                        playlist = Playlist(p_data['name'])
                        for s_data in p_data['songs']:
                            song = Song(s_data['name'], s_data['singer'], s_data['genre'])
                            playlist.add_song(song)
                        playlists.append(playlist)
                print(f"Playlists imported from {filename}")
            except FileNotFoundError:
                print("File not found.")
            except json.JSONDecodeError:
                print("Invalid file format.")
        elif choice == "12":
            # Display all playlists and songs
            if not playlists:
                print("No playlists available.")
            else:
                for p in playlists:
                    print(f"\n{p}")
        elif choice == "13":
            save_playlists(playlists)
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 13.")


if __name__ == "__main__":
    main()
