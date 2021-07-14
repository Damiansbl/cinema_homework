class Room1:
    @staticmethod
    def get_room():
        return "Room 1"

    @staticmethod
    def get_seating_plan():
        return range(8), "ABCDEF"


class Room2:
    @staticmethod
    def get_room():
        return "Room 2"

    @staticmethod
    def get_seating_plan():
        return range(16), "ABCDEFGHIJKL"
