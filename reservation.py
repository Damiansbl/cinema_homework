from pprint import pprint as pp
from datetime import datetime
from Seance import Seance
from Rooms import Room1
from Rooms import Room2



# Execution
room1 = Room1()
room2 = Room2()
s1 = Seance("Psy", datetime(2021, 7, 15, 19, 00), room1)
s2 = Seance("Skyfall", datetime(2021, 7, 15, 20, 00), room2)
pp(s1.seats)
