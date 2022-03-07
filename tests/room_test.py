import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1)

    def test_has_room_number(self):
        self.assertEqual(1, self.room_1.room_number)


