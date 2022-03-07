

class Guest:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def check_in(self, room): 
        return f"{self.name} {self.surname} is checked in in room {room.room_number}"

    def check_out(self, room): 
        return f"{self.name} {self.surname} is checked out from the {room.room_number}"

