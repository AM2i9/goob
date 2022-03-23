import json

import pygame

from game.room import Room
from game.triggers.button import Button
from game.traps.spike import SpikeTrap
from game.level import Level

pygame.init()
pygame.display.init()
pygame.display.set_mode((0,0))

room_1 = Room(595, 660, 30, 30, "assets/test_map.png")
room_2 = Room(595, 660, 655, 30, "assets/test_map_2.png", sprite_startpoint=(261, 282))

button = Button(111, 200, 44, 44)
room_1.add_trap(
    SpikeTrap(111, 200, trigger=button)
)
room_2.add_trigger(button)

button2 = Button(412, 275, 44, 44)
room_1.add_trap(
    SpikeTrap(412, 375, trigger=button2)
)
room_2.add_trigger(button2)

level = Level(0, room_1, room_2)

with open('level.json', 'w') as f:
    json.dump(level.to_dict(), f, indent=4)