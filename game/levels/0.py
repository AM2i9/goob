from game.coin import Coin
from game.level import Level
from game.traps.spike import SpikeTrap
from game.triggers.button import Button
from game.wall import Wall, WallType


def build_level(room_1, room_2):

    level = Level(0, room_1, room_2, end_coin=Coin())

    button = Button()

    room_1.set_tile(2, 2, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(3, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(4, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(6, 2, Wall(WallType.DL_LJUNCT))

    room_1.set_tile(2, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(2, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(2, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 5, Wall(WallType.VERTICAL))

    room_1.set_tile(2, 6, Wall(WallType.UR_LJUNCT))
    room_1.set_tile(3, 6, Wall(WallType.HORIZONTAL_RIGHT_END))
    room_1.set_tile(5, 6, Wall(WallType.HORIZONTAL_LEFT_END))
    room_1.set_tile(6, 6, Wall(WallType.UL_LJUNCT))


    room_2.set_tile(2, 2, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(3, 2, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4, 2, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 2, Wall(WallType.HORIZONTAL))
    room_2.set_tile(6, 2, Wall(WallType.DL_LJUNCT))

    room_2.set_tile(2, 3, Wall(WallType.VERTICAL))
    room_2.set_tile(2, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(2, 5, Wall(WallType.VERTICAL))
    room_2.set_tile(6, 3, Wall(WallType.VERTICAL))
    room_2.set_tile(6, 4, Wall(WallType.L_TJUNCT))
    room_2.set_tile(5, 4, Wall(WallType.HORIZONTAL_LEFT_END))
    room_2.set_tile(6, 5, Wall(WallType.VERTICAL))

    room_2.set_tile(2, 6, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(3, 6, Wall(WallType.HORIZONTAL_RIGHT_END))
    room_2.set_tile(5, 6, Wall(WallType.HORIZONTAL_LEFT_END))
    room_2.set_tile(6, 6, Wall(WallType.UL_LJUNCT))

    room_1.set_tile(4, 6, SpikeTrap(trigger=button))
    room_2.set_tile(4, 6, button)

    room_1.set_tile(4, 8, level.end_coin)

    return level
