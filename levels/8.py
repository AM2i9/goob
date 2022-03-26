from game.coin import Coin
from game.level import Level
from game.traps.spike import SpikeTrap
from game.triggers.button import Button
from game.wall import Wall, WallType


def build_level(room_1, room_2):

    level = Level(8, room_1, room_2, end_coin=Coin())

    buttons = [
        [Button() for _ in range(9)] for _ in range(10)
    ]
    
    button_rows = [
                [0,0,0,0,0,0,0,0,0],
                [0,-1,-1,-1,0,-1,0,-1,0],
                [0,-1,0,-1,0,-1,0,-1,0],
                [0,-1,0,-1,0,-1,0,-1,0],
                [0,-1,0,-1,0,-1,0,-1,0],
                [0,-1,0,-1,0,-1,0,-1,0],
                [0,-1,0,-1,0,-1,0,-1,0],
                [0,-1,0,-1,0,-1,0,-1,0],
                [0,-1,0,-1,-1,-1,0,-1,0],
                [0,0,0,0,0,0,0,0,0],
            ]

    r, c = 0, 0
    for _ in range(10*9):
        if button_rows[r][c] == 0:
            room_2.set_tile(c, r, buttons[r][c])
        room_1.set_tile(c, r, SpikeTrap(buttons[r][c]))
        r += 1
        if r == 10:
            c += 1
            r = 0
    
    room_2.set_tile(6, 4, Button())

    room_1.set_tile(7, 8, level.end_coin)

    room_1.sprite_startpoint = (64 * 1, 64 * 8)
    room_2.sprite_startpoint = (64 * 1, 64 * 8)


    return level
