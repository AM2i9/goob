from typing import List, Tuple
from dataclasses import dataclass

from game.room import Room
from game.traps import TRAPS
from game.triggers import TRIGGERS

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

    @classmethod
    def from_dict(cls, data):
        room_1 = Room.from_dict(data["room_1"], 0)
        room_2 = Room.from_dict(data["room_2"], 1)
        
        for trap in data["room_1"]["traps"]:
            trap_trig = TRIGGERS.get(trap["trigger"]["type"])(
                trap["trigger"]["left"],
                trap["trigger"]["top"],
                trap["trigger"]["width"],
                trap["trigger"]["height"],
                trap["trigger"]["visible_default"],
            )

            trap_obj = TRAPS.get(trap["type"])(
                trap["left"],
                trap["top"],
                trap["width"],
                trap["height"],
                trigger=trap_trig,
            )

            if trap["trigger"]["in_room"]:
                room_1.add_trigger(trap_trig)
            else:
                room_2.add_trigger(trap_trig)
            
            room_1.add_trap(trap_obj)

        for trap in data["room_2"]["traps"]:
            trap_trig = TRIGGERS.get(trap["trigger"]["type"])(
                trap["trigger"]["left"],
                trap["trigger"]["top"],
                trap["trigger"]["width"],
                trap["trigger"]["height"],
                trap["trigger"]["visible_default"],
            )

            trap_obj = TRAPS.get(trap["type"])(
                trap["left"],
                trap["top"],
                trap["width"],
                trap["height"],
                trigger=trap_trig,
            )

            if trap["trigger"]["in_room"]:
                room_2.add_trigger(trap_trig)
            else:
                room_1.add_trigger(trap_trig)
            
            room_2.add_trap(trap_obj)

        return cls(
            id=data["id"],
            room_1=room_1,
            room_2=room_2,
        )
        
