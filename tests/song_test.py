import imp
import unittest
from classes.songs import Song
from classes.room import Room

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Material Girl", "Madonna")

    def test_song_has_title(self):
        self.assertEqual("Material Girl", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Madonna", self.song_1.artist)

    def test_add_song_to_room(self):
        self.room = Room(1)
        adding_song = self.song_1.add_songs_to_room(self.room)
        self.assertEqual("Material Girl by Madonna has been added to room 1", adding_song)
