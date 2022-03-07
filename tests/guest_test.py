import unittest
from classes.guest import *
from classes.room import*

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Katya", "Patton")

    def test_guest_has_name(self):
        self.assertEqual("Katya", self.guest_1.name)

    def test_guest_has_surname(self):
        self.assertEqual("Patton", self.guest_1.surname)

    def test_check_in_guest(self):
        self.room_1 = Room(1)
        check_in_room = self.guest_1.check_in(self.room_1)
        self.assertEqual("Katya Patton is checked in in room 1", check_in_room)


    def test_check_in_guest(self):
        self.room_1 = Room(1)
        check_in_room = self.guest_1.check_out(self.room_1)
        self.assertEqual("Katya Patton is checked out from the 1", check_in_room)

        