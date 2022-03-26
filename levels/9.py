from game.coin import Coin
from game.level import Level
from game.traps.spike import SpikeTrap
from game.triggers.button import Button
from game.wall import Wall, WallType


def build_level(room_1, room_2):

    level = Level(8, room_1, room_2, end_coin=Coin())

    button_1 = Button()
    button_2 = Button()
    button_3 = Button()
    button_4 = Button()
    button_5 = Button()
    button_6 = Button()
    button_7 = Button()

    room_1.set_tile(2, 1, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(3, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(4, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(6, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(7, 1, Wall(WallType.HORIZONTAL))
    room_1.set_tile(8, 1, Wall(WallType.DL_LJUNCT))
    room_1.set_tile(0, 2, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(1, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(2, 2, Wall(WallType.L_TJUNCT))
    room_1.set_tile(8, 2, Wall(WallType.VERTICAL))
    room_1.set_tile(0, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(2, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(4, 3, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(5, 3, Wall(WallType.HORIZONTAL))
    room_1.set_tile(6, 3, Wall(WallType.DL_LJUNCT))
    room_1.set_tile(8, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(0, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(2, 4, Wall(WallType.VERTICAL_BOTTOM_END))
    room_1.set_tile(4, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 4, Wall(WallType.VERTICAL_BOTTOM_END))
    room_1.set_tile(8, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(0, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(4, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(8, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(0, 6, Wall(WallType.R_TJUNCT))
    room_1.set_tile(1, 6, Wall(WallType.HORIZONTAL))
    room_1.set_tile(2, 6, Wall(WallType.HORIZONTAL))
    room_1.set_tile(3, 6, Wall(WallType.D_TJUNCT))
    room_1.set_tile(4, 6, Wall(WallType.UL_LJUNCT))
    room_1.set_tile(6, 6, Wall(WallType.VERTICAL_TOP_END))
    room_1.set_tile(8, 6, Wall(WallType.VERTICAL))
    room_1.set_tile(0, 7, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 7, Wall(WallType.VERTICAL_BOTTOM_END))
    room_1.set_tile(6, 7, Wall(WallType.R_TJUNCT))
    room_1.set_tile(7, 7, Wall(WallType.HORIZONTAL))
    room_1.set_tile(8, 7, Wall(WallType.UL_LJUNCT))
    room_1.set_tile(0, 8, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 8, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(6, 8, Wall(WallType.UL_LJUNCT))
    room_1.set_tile(0, 9, Wall(WallType.UR_LJUNCT))
    room_1.set_tile(1, 9, Wall(WallType.HORIZONTAL))
    room_1.set_tile(2, 9, Wall(WallType.HORIZONTAL))
    room_1.set_tile(3, 9, Wall(WallType.HORIZONTAL))
    room_1.set_tile(4, 9, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 9, Wall(WallType.UL_LJUNCT))

    room_2.set_tile(2, 1, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(3, 1, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4, 1, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 1, Wall(WallType.DL_LJUNCT))
    room_2.set_tile(0, 2, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(1, 2, Wall(WallType.HORIZONTAL))
    room_2.set_tile(2, 2, Wall(WallType.L_TJUNCT))
    room_2.set_tile(5, 2, Wall(WallType.VERTICAL))
    room_2.set_tile(0, 3, Wall(WallType.VERTICAL))
    room_2.set_tile(2, 3, Wall(WallType.VERTICAL_BOTTOM_END))
    room_2.set_tile(4, 3, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(5, 3, Wall(WallType.U_TJUNCT))
    room_2.set_tile(6, 3, Wall(WallType.DL_LJUNCT))
    room_2.set_tile(0, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(4, 4, Wall(WallType.VERTICAL_BOTTOM_END))
    room_2.set_tile(6, 4, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(7, 4, Wall(WallType.HORIZONTAL))
    room_2.set_tile(8, 4, Wall(WallType.DL_LJUNCT))
    room_2.set_tile(0, 5, Wall(WallType.VERTICAL))
    room_2.set_tile(2, 5, Wall(WallType.VERTICAL_TOP_END))
    room_2.set_tile(8, 5, Wall(WallType.VERTICAL))
    room_2.set_tile(0, 6, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(1, 6, Wall(WallType.HORIZONTAL))
    room_2.set_tile(2, 6, Wall(WallType.L_TJUNCT))
    room_2.set_tile(6, 6, Wall(WallType.VERTICAL_TOP_END))
    room_2.set_tile(8, 6, Wall(WallType.VERTICAL))
    room_2.set_tile(2, 7, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(3, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(6, 7, Wall(WallType.U_TJUNCT))
    room_2.set_tile(7, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(8, 7, Wall(WallType.UL_LJUNCT))


    room_1.set_tile(1, 5, SpikeTrap(button_1))
    room_2.set_tile(1, 5, button_1)

    room_1.set_tile(2, 5, SpikeTrap(button_2))
    room_2.set_tile(3, 5, button_2)

    room_1.set_tile(3, 5, SpikeTrap(button_3))
    room_2.set_tile(3, 4, button_3)

    room_1.set_tile(3, 5, SpikeTrap(button_3))
    room_2.set_tile(3, 4, button_3)

    room_1.set_tile(4, 2, SpikeTrap(button_4))
    room_2.set_tile(4, 2, button_4)

    room_1.set_tile(6, 5, SpikeTrap(button_5))
    room_2.set_tile(3, 6, button_5)

    room_1.set_tile(6, 2, SpikeTrap(button_6))
    room_2.set_tile(5, 4, button_6)

    room_1.set_tile(3, 8, SpikeTrap(button_7))
    room_2.set_tile(7, 6, button_7)

    room_1.set_tile(1, 7, level.end_coin)


    room_1.sprite_startpoint = (64 * 1, 64 * 3)
    room_2.sprite_startpoint = (64 * 1, 64 * 3)

    return level
