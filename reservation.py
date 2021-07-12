from pprint import pprint as pp


class Seance:
    def __init__(self, title, hour, room):
        self.title = title
        self.hour = hour
        self.room = room

        rows, letters = self.room.get_seating_plan()
        self.seats = [{letter: None for letter in letters} for _ in rows]

    def get_room_name(self):
        return self.room.get_room()

    def _parse_seat(self, seat):
        rows, letters = self.room.get_seating_plan()
        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f"Invalid seat letter: {letter}")

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text}")

        if row not in rows:
            raise ValueError(f"Row number is out of seating range: {row}")

        return row, letter

    def assign_passenger(self, seat="2C", passenger="Tytus Bomba"):
        row, letter = self._parse_seat(seat)
        self.seats[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)

        if self.seats[row_from][letter_from] is None:
            raise ValueError(f'No passenger assigned to place {seat_from}')

        row_to, letter_to = self._parse_seat(seat_to)

        if self.seats[row_to][letter_to] is not None:
            raise ValueError(f'Seat {seat_to} is already taken')

        self.seats[row_to][letter_to] = self.seats[row_from][letter_from]
        self.seats[row_from][letter_from] = None


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

# Testing
room1 = Room1()
room2 = Room2()
s1 = Seance("Psy", 19, room1)
s2 = Seance("Skyfall", 20, room2)
pp(s1.seats)