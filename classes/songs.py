class Song:
    
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def add_songs_to_room(self, title, artist, room):
        return f"{self.title} by {self.artist} has been added to room {room}"