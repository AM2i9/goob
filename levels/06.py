from game.coin import Coin
from game.level import Level
from game.traps.spike import SpikeTrap
from game.triggers.button import Button
from game.wall import Wall, WallType


def build_level(room_1, room_2):

    level = Level(6, room_1, room_2, end_coin=Coin())

    button_1 = Button()
    button_2 = Button()
    button_3 = Button()
    button_4 = Button()

    room_1.set_tile(3, 1, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(4, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 1, Wall(WallType.DL_LJUNCT))
    room_1.set_tile(3, 2, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 2, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 6, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 6, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 7, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 7, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 8, Wall(WallType.UR_LJUNCT))
    room_1.set_tile(4, 8, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 8, Wall(WallType.UL_LJUNCT))

    room_1.set_tile(4, 6, SpikeTrap(button_3))
    room_1.set_tile(4, 5, SpikeTrap(button_1))
    room_1.set_tile(4, 4, SpikeTrap(button_2))
    room_1.set_tile(4, 3, SpikeTrap(button_4))

    room_2.set_tile(3, 1, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(4, 1, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 1, Wall(WallType.DL_LJUNCT))

    room_2.set_tile(3, 2, Wall(WallType.VERTICAL))
    room_2.set_tile(5, 2, Wall(WallType.VERTICAL))

    room_2.set_tile(2, 3, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(3, 3, Wall(WallType.UL_LJUNCT))
    room_2.set_tile(5, 3, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(6, 3, Wall(WallType.DL_LJUNCT))

    room_2.set_tile(2, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(3, 4, button_2)
    room_2.set_tile(4, 5, button_1)
    room_2.set_tile(5, 4, button_3)
    room_2.set_tile(6, 4, Wall(WallType.VERTICAL))

    room_2.set_tile(2, 5, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(3, 5, Wall(WallType.DL_LJUNCT))
    room_2.set_tile(5, 5, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(6, 5, Wall(WallType.UL_LJUNCT))

    room_2.set_tile(3, 6, Wall(WallType.VERTICAL))
    room_2.set_tile(4, 6, button_4)
    room_2.set_tile(5, 6, Wall(WallType.VERTICAL))

    room_2.set_tile(3, 7, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(4, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 7, Wall(WallType.UL_LJUNCT))

    room_1.set_tile(4, 7, level.end_coin)

    room_1.sprite_startpoint = (64 * 4, 64 * 2)

    return level
