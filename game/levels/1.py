from game.coin import Coin
from game.level import Level
from game.traps.spike import SpikeTrap
from game.triggers.button import Button
from game.wall import Wall, WallType


def build_level(room_1, room_2):

    level = Level(1, room_1, room_2, end_coin=Coin())

    button_1 = Button()
    button_2 = Button()

    room_1.set_tile(2, 2, Wall(WallType.VERTICAL_TOP_END))
    room_1.set_tile(3, 2, SpikeTrap(trigger=button_1))
    room_1.set_tile(4, 2, Wall(WallType.SINGLE))
    room_1.set_tile(5, 2, SpikeTrap(trigger=button_2))
    room_1.set_tile(6, 2, Wall(WallType.VERTICAL_TOP_END))

    room_1.set_tile(2, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(2, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(4, 4, Wall(WallType.SINGLE))
    room_1.set_tile(2, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 5, Wall(WallType.VERTICAL))

    room_1.set_tile(2, 6, Wall(WallType.UR_LJUNCT))
    room_1.set_tile(3, 6, Wall(WallType.HORIZONTAL))
    room_1.set_tile(4, 6, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 6, Wall(WallType.HORIZONTAL))
    room_1.set_tile(6, 6, Wall(WallType.UL_LJUNCT))

    room_2.set_tile(2, 2, Wall(WallType.VERTICAL_TOP_END))
    room_2.set_tile(3, 2, button_1)
    room_2.set_tile(4, 2, Wall(WallType.VERTICAL_TOP_END))
    room_2.set_tile(5, 2, button_2)
    room_2.set_tile(6, 2, Wall(WallType.VERTICAL_TOP_END))

    room_2.set_tile(2, 3, Wall(WallType.VERTICAL))
    room_2.set_tile(4, 3, Wall(WallType.VERTICAL))
    room_2.set_tile(4, 4, Wall(WallType.VERTICAL_BOTTOM_END))
    room_2.set_tile(2, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(2, 5, Wall(WallType.VERTICAL))
    room_2.set_tile(6, 3, Wall(WallType.VERTICAL))
    room_2.set_tile(6, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(6, 5, Wall(WallType.VERTICAL))

    room_2.set_tile(2, 6, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(3, 6, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4, 6, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 6, Wall(WallType.HORIZONTAL))
    room_2.set_tile(6, 6, Wall(WallType.UL_LJUNCT))

    room_1.set_tile(4, 1, level.end_coin)

    room_1.sprite_startpoint = (64 * 4, 64 * 5)
    room_2.sprite_startpoint = (64 * 4, 64 * 5)

    return level
