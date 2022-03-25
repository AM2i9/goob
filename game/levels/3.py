from game.coin import Coin
from game.level import Level
from game.traps.spike import SpikeTrap
from game.triggers.button import Button
from game.wall import Wall, WallType


def build_level(room_1, room_2):

    level = Level(0, room_1, room_2, end_coin=Coin())

    button_1 = Button()
    button_2 = Button()
    button_3 = Button()

    room_1.set_tile(0, 3, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(0, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(1, 4, level.end_coin)
    room_1.set_tile(0, 5, Wall(WallType.UR_LJUNCT))

    for i in range(1, 8):
        room_1.set_tile(i, 3, Wall(WallType.HORIZONTAL))
        room_1.set_tile(i, 5, Wall(WallType.HORIZONTAL))
    
    room_1.set_tile(4, 3, None)
    room_1.set_tile(3, 3, Wall(WallType.UL_LJUNCT))
    room_1.set_tile(5, 3, Wall(WallType.UR_LJUNCT))
    room_1.set_tile(3, 2, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(5, 2, Wall(WallType.DL_LJUNCT))
    room_1.set_tile(4, 2, Wall(WallType.HORIZONTAL))

    room_1.set_tile(8, 3, Wall(WallType.DL_LJUNCT))
    room_1.set_tile(8, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(8, 5, Wall(WallType.UL_LJUNCT))

    room_1.set_tile(3, 4, SpikeTrap(button_3))
    room_1.set_tile(4, 4, SpikeTrap(button_2))
    room_1.set_tile(5, 4, SpikeTrap(button_1))

    room_2.set_tile(3,4, button_3)
    room_2.set_tile(3,5, button_2)
    room_2.set_tile(3,6, button_1)

    room_2.set_tile(2,3, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(2,5, Wall(WallType.VERTICAL))
    room_2.set_tile(2,4, Wall(WallType.VERTICAL))
    room_2.set_tile(2,6, Wall(WallType.VERTICAL))
    room_2.set_tile(2,7, Wall(WallType.UR_LJUNCT))

    room_2.set_tile(5,3, Wall(WallType.DL_LJUNCT))
    room_2.set_tile(5,5, Wall(WallType.VERTICAL))
    room_2.set_tile(5,4, Wall(WallType.VERTICAL))
    room_2.set_tile(5,6, Wall(WallType.VERTICAL))
    room_2.set_tile(5,7, Wall(WallType.UL_LJUNCT))

    room_2.set_tile(3,3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4,3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(3,7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4,7, Wall(WallType.HORIZONTAL))

    room_1.sprite_startpoint = (64 * 7, 64 * 4)

    return level
