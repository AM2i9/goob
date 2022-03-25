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

    room_1.set_tile(1, 2, Wall(WallType.DR_LJUNCT))
    room_1.set_tile(2, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(3, 2, Wall(WallType.D_TJUNCT))
    room_1.set_tile(4, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(6, 2, Wall(WallType.HORIZONTAL))
    room_1.set_tile(7, 2, Wall(WallType.DL_LJUNCT))

    room_1.set_tile(1, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(2, 3, level.end_coin)
    room_1.set_tile(3, 3, Wall(WallType.VERTICAL))
    room_1.set_tile(6, 3, SpikeTrap(button_1))
    room_1.set_tile(7, 3, Wall(WallType.VERTICAL))

    room_1.set_tile(1, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 4, Wall(WallType.VERTICAL))
    room_1.set_tile(5, 4, Wall(WallType.VERTICAL_TOP_END))
    room_1.set_tile(7, 4, Wall(WallType.VERTICAL))

    room_1.set_tile(1, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(3, 5, Wall(WallType.VERTICAL_BOTTOM_END))
    room_1.set_tile(4, 5, SpikeTrap(button_3))
    room_1.set_tile(5, 5, Wall(WallType.VERTICAL))
    room_1.set_tile(7, 5, Wall(WallType.VERTICAL))

    room_1.set_tile(1, 6, Wall(WallType.VERTICAL))
    room_1.set_tile(2, 6, SpikeTrap(button_2))
    room_1.set_tile(5, 6, Wall(WallType.VERTICAL))
    room_1.set_tile(7, 6, Wall(WallType.VERTICAL))

    room_1.set_tile(1, 7, Wall(WallType.UR_LJUNCT))
    room_1.set_tile(2, 7, Wall(WallType.HORIZONTAL))
    room_1.set_tile(3, 7, Wall(WallType.HORIZONTAL))
    room_1.set_tile(4, 7, Wall(WallType.HORIZONTAL))
    room_1.set_tile(5, 7, Wall(WallType.U_TJUNCT))
    room_1.set_tile(6, 7, Wall(WallType.HORIZONTAL))
    room_1.set_tile(7, 7, Wall(WallType.UL_LJUNCT))

    room_2.set_tile(5, 2, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(6, 2, Wall(WallType.HORIZONTAL))
    room_2.set_tile(7, 2, Wall(WallType.DL_LJUNCT))
    
    room_2.set_tile(1, 3, Wall(WallType.DR_LJUNCT))
    room_2.set_tile(2, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(3, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(4, 3, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 3, Wall(WallType.L_TJUNCT))
    room_2.set_tile(6, 3, button_1)
    room_2.set_tile(7, 3, Wall(WallType.VERTICAL))

    room_2.set_tile(1, 4, Wall(WallType.VERTICAL))
    room_2.set_tile(5, 4, Wall(WallType.VERTICAL_BOTTOM_END))
    room_2.set_tile(7, 4, Wall(WallType.VERTICAL))

    room_2.set_tile(1, 5, Wall(WallType.VERTICAL))
    room_2.set_tile(3, 5, Wall(WallType.VERTICAL_TOP_END))
    room_2.set_tile(7, 5, Wall(WallType.VERTICAL))

    room_2.set_tile(1, 6, Wall(WallType.VERTICAL))
    room_2.set_tile(2, 6, button_2)
    room_2.set_tile(3, 6, Wall(WallType.VERTICAL))
    room_2.set_tile(4, 6, button_3)
    room_2.set_tile(5, 6, Wall(WallType.VERTICAL_TOP_END))
    room_2.set_tile(7, 6, Wall(WallType.VERTICAL))

    room_2.set_tile(1, 7, Wall(WallType.UR_LJUNCT))
    room_2.set_tile(2, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(3, 7, Wall(WallType.U_TJUNCT))
    room_2.set_tile(4, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(5, 7, Wall(WallType.U_TJUNCT))
    room_2.set_tile(6, 7, Wall(WallType.HORIZONTAL))
    room_2.set_tile(7, 7, Wall(WallType.UL_LJUNCT))
    
    
    room_1.sprite_startpoint = (64 * 6, 64 * 6)
    room_2.sprite_startpoint = (64 * 6, 64 * 6)

    return level
