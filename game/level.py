from typing import List, Tuple
from dataclasses import dataclass

from game.room import Room

@dataclass
class Level:

    id: int

    room_1: Room
    room_2: Room

    def reset(self, good_twin, evil_twin):
        good_twin.rect.update(*self.room_1.sprite_startpoint, good_twin.rect.width, good_twin.rect.height)
        evil_twin.rect.update(*self.room_2.sprite_startpoint, evil_twin.rect.width, evil_twin.rect.height)
        good_twin.is_dead = False
        evil_twin.is_dead = False

    def draw(self, win, good_twin, evil_twin):
        self.room_1.fill((64, 77, 88))
        self.room_2.fill((88, 64, 64))

        self.room_1.draw(win, good_twin)
        self.room_2.draw(win, evil_twin)

    def to_dict(self):
        return {
            "id": self.id,
            "room_1": self.room_1.to_dict(),
            "room_2": self.room_2.to_dict(),
        }

        
