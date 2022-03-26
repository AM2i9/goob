from game.coin import Coin
from game.level import Level
from game.traps.spike import SpikeTrap
from game.triggers.button import Button
from game.wall import Wall, WallType


def build_level(room_1, room_2):

    level = Level(5, room_1, room_2, end_coin=Coin())

    button_1 = Button()
    button_2 = Button()
    button_3 = Button()
    button_4 = Button()
    button_5 = Button()


    room_1.set_tile(1, 1, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(2, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(3, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(4, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(6, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(7, 1, Wall(WallType.DL_LJUNCT))
    room_1.set_tile(1, 2, Wall(WallType.VERTICAL))
    room_1.set_tile(4, 2, SpikeTrap(button_4))
    room_1.set_tile(7, 2, Wall(WallType.VERTICAL))
    room_1.set_tile(1, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 3, Wall(WallType.VERTICAL_TOP_END))
    room_1.set_tile(4, 3, SpikeTrap(button_5))
    room_1.set_tile(5, 3, Wall(WallType.VERTICAL_TOP_END))
    room_1.set_tile(7, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(1, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(4, 4, level.end_coin)
    room_1.set_tile(5, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(7, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(1, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 5, Wall(WallType.R_TJUNCT))
    room_1.set_tile(4, 5, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 5, Wall(WallType.L_TJUNCT))
    room_1.set_tile(7, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(1, 6, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 6, Wall(WallType.VERTICAL_BOTTOM_END))
    room_1.set_tile(5, 6, Wall(WallType.VERTICAL_BOTTOM_END))
    room_1.set_tile(7, 6, Wall(WallType.VERTICAL))
    room_1.set_tile(1, 7, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 7, SpikeTrap(button_2))
    room_1.set_tile(4, 7, SpikeTrap(button_1))
    room_1.set_tile(5, 7, SpikeTrap(button_3))
    room_1.set_tile(7, 7, Wall(WallType.VERTICAL))
    room_1.set_tile(1, 8, Wall(WallType.UR_LJUNCT))
    room_1.set_tile(2, 8, Wall(WallType.HORIZONTAL))
    room_1.set_tile(3, 8, Wall(WallType.HORIZONTAL))
    room_1.set_tile(4, 8, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 8, Wall(WallType.HORIZONTAL))
    room_1.set_tile(6, 8, Wall(WallType.HORIZONTAL))
    room_1.set_tile(7, 8, Wall(WallType.UL_LJUNCT))

    room_2.set_tile(1, 3, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(2, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(3, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(6, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(7, 3, Wall(WallType.DL_LJUNCT))
    room_2.set_tile(1, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(3, 4, button_2)
    room_2.set_tile(5, 4, button_3)
    room_2.set_tile(6, 4, button_4)
    room_2.set_tile(7, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(1, 5, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(2, 5, Wall(WallType.HORIZONTAL))
    room_2.set_tile(2, 4, button_5)
    room_2.set_tile(3, 5, Wall(WallType.DL_LJUNCT))
    room_2.set_tile(4, 5, button_1)
    room_2.set_tile(5, 5, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(6, 5, Wall(WallType.HORIZONTAL))
    room_2.set_tile(7, 5, Wall(WallType.UL_LJUNCT))

    room_2.set_tile(3, 6, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(4, 6, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 6, Wall(WallType.UL_LJUNCT))



    room_1.sprite_startpoint = (64 * 4, 64 * 6)
    room_2.sprite_startpoint = (64 * 4, 64 * 4)

    return level
