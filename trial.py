from fastapi import FastAPI
from dataclasses import dataclass

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@dataclass
class Song:
    song_id: int
    song_name: str
    rate: int
    comment: str

    def __str__(self):
        return (f"ID: {self.song_id}, Name: '{self.song_name}', "
                f"Rate: {self.rate}, Comment: '{self.comment}'")

# Initialize an empty list to store songs
songs_list = []

def add_song():
    while True:
        try:
            # Collect song ID
            song_id = int(input("Enter Song ID (integer): "))
            # Check for duplicate ID
            if any(song.song_id == song_id for song in songs_list):
                raise ValueError("Song ID already exists. Please enter a unique ID.")
            
            # Collect song name
            song_name = input("Enter Song Name: ").strip()
            if not song_name:
                raise ValueError("Song name cannot be empty.")
            
            # Collect rate
            rate = int(input("Enter Rate (0-5): "))
            if rate < 0 or rate > 5:
                raise ValueError("Rate must be between 0 and 5.")
            
            # Collect comment
            comment = input("Enter Comment: ").strip()
            
            # Create a Song instance
            new_song = Song(song_id, song_name, rate, comment)
            
            # Add to the list
            songs_list.append(new_song)
            
            print("\nSong added successfully!\n")
            
            # Display the updated list
            display_songs()
            
        except ValueError as ve:
            print(f"Input Error: {ve}. Please try again.\n")
            continue
        
        # Ask if the user wants to exit
        exit_choice = input("Do you want to exit the Song Manager? (y/n): ").strip().lower()
        if exit_choice == 'y':
            print("\nThank you for using the Song Manager! Goodbye!")
            break
        else:
            print("\nLet's add another song.\n")

def display_songs():
    if not songs_list:
        print("\nNo songs to display.\n")
        return
    
    print("Current List of Songs:")
    print("-" * 50)
    for song in songs_list:
        print(song)
    print("-" * 50 + "\n")

def main():
    print("Welcome to the Song Manager!\n")
    add_song()

if __name__ == "__main__":
    main()

