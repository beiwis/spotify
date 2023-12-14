from dotenv import load_dotenv
import API_requests as api
import os
import csv
import glob
import datetime

load_dotenv()
username = os.getenv('SPOTIPY_USERNAME')

def main():
    print("                             dP   oo .8888b               dP                     dP          \n                             88      88   '               88                     88          \n.d8888b. 88d888b. .d8888b. d8888P dP 88aaa  dP    dP    d8888P .d8888b. .d8888b. 88 .d8888b. \nY8ooooo. 88'  `88 88'  `88   88   88 88     88    88      88   88'  `88 88'  `88 88 Y8ooooo. \n      88 88.  .88 88.  .88   88   88 88     88.  .88      88   88.  .88 88.  .88 88       88 \n`88888P' 88Y888P' `88888P'   dP   dP dP     `8888P88      dP   `88888P' `88888P' dP `88888P' \n         88                                      .88                                         \n         dP                                  d8888P")
    if username:
        print(f"Welcome {username}!, please choose a mode:")
    else:
        print("Please set your Spotify username in the .env file. See README.md for more information.")
        return
    while True:
        mode = input("Enter the mode number (q to quit): ")

        if mode == "q":
            break
        
        if mode == "0":
            api.get_genres()
        if mode == "1":
            tidy_up_songs()
        elif mode == "2":
            create_playlist() #TODO: Implement this function
        elif mode == "3":
            get_song_statistics() #TODO: Implement this function
        else:
            print("Invalid mode number. Please try again.")

def format_timestamp(timestamp):
    datetime_obj = datetime.datetime.strptime(timestamp, "%d%m%Y_%H%M%S")
    formatted_timestamp = datetime_obj.strftime("%H:%M:%S (%d/%m/%Y)")
    return formatted_timestamp

def tidy_up_songs():
    csv_files = glob.glob(f"*{username}*.csv")
    if not csv_files:
        print(f"No CSV file found for username: {username}")
        input("Would you like to load a new CSV file? (y/n): ")
        if confirm.lower() == "y":
            api.get_saved_songs()
        return

    csv_files.sort(key=os.path.getmtime, reverse=True)
    most_recent_csv = csv_files[0]
    timestamp = os.path.splitext(most_recent_csv)[0].split("_")[-2:]  # Extract the last two elements separated by "_"
    timestamp = "_".join(timestamp)  # Join the elements back with "_"
    formatted_timestamp = format_timestamp(timestamp)
    #FIXME: filter the wrong inputs:
    confirm = input(f"The last file found is from {formatted_timestamp} is this the file you want to use? (y/n): ")
    if confirm.lower() != "y":
        input("Would you like to load a new CSV file? (y/n): ")
        if confirm.lower() == "y":
            api.get_saved_songs()
        return
    tidy_songs(most_recent_csv)

def tidy_songs(csv_file):
    """Tidy up songs in a CSV file"""
    with open(csv_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            song_id = row[3]  # The song ID is in the fourth column
            print(f"Current song: {row[0]} by {row[1]}")
            confirm = input("Do you want to listen to it? (y/n): ")
            if confirm.lower() == "y":
                api.add_song_queue(song_id)
                print("Song added to queue!")
            tidy_song(song_id)

def tidy_song(song_id):
    """Places a song in a playlist based on vibes, genre, etc."""
    ######################## Genre ########################
    genre = input("What genre is this song? (e.g. pop, rock, rap, etc.): ")
    if valid_genre(genre):
        print(f"Adding song to {genre} playlist...")
        api.add_song_to_playlist(song_id, genre)
        #TODO: sub-genres could be added here
    else:
        print("No genre specified. Skipping...")
    ######################## Vibes ########################
    vibes = input("What vibes does this song have? (e.g. sad, happy, chill, etc.): ")
    if valid_vibes(vibes):
        vibes_dict = {
            "sad": ["heartbroken", "melancholic", "nostalgic"],
            "happy": ["uplifting", "energetic", "joyful"],
            "chill": ["relaxed", "calm", "peaceful"]
        }
        if vibes in vibes_dict:
            specific_vibes = vibes_dict[vibes]
            print(f"Adding song to {vibes} playlist...")
            for specific_vibe in specific_vibes:
                api.add_song_to_playlist(song_id, specific_vibe)
        else:
            print("Invalid vibes specified. Skipping...")
    else:
        print("No vibes specified. Skipping...")
    pass

def valid_genre(genre):
    """Checks if a string corresponds to a valid genre"""
    pass

def valid_vibes(vibes):
    """Checks if a string corresponds to a valid vibe"""
    pass

def create_playlist():
    """Create a playlist based on criteria"""

    # TODO: Implement the logic to create a playlist based on criteria
    pass

def get_song_statistics():
    # TODO: Implement the logic to get song statistics
    pass

if __name__ == "__main__":
    main()
