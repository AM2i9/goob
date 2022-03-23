import json

import pygame
from pygame.locals import *
from game.level import Level

from game.room import Room
from game.triggers.button import Button
from game.twin import Twin
from game.traps.spike import SpikeTrap

def run_game():
    pygame.init()

    win = pygame.display.set_mode(size=(1280, 720))
    clock = pygame.time.Clock()

    room_1 = Room(0, "assets/level0/level0_0.png")
    room_2 = Room(1, "assets/level0/level0_1.png")

    button = Button(272, 525, 44, 44, True)
    room_1.add_trap(SpikeTrap(272, 525, trigger=button))
    room_2.add_trigger(button)

    level = Level(0, room_1, room_2)

    good_guy = Twin(level.room_1)
    bad_guy = Twin(level.room_2)

    x = 0
    y = 0

    print(level.to_dict())
    level.reset(good_guy, bad_guy)
    while True:

        if good_guy.is_dead or bad_guy.is_dead:
            level.reset(good_guy, bad_guy)
            clock
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    x = 10
                elif event.key == K_LEFT:
                    x = -10
                if event.key == K_UP:
                    y = -10
                elif event.key == K_DOWN:
                    y = 10
            elif event.type == KEYUP:
                if event.key in (K_RIGHT, K_LEFT):
                    x = 0
                if event.key in (K_UP, K_DOWN):
                    y = 0

        win.fill(0)

        good_guy.move(x, y)
        bad_guy.move(x, y)

        level.draw(win, good_guy, bad_guy)

        pygame.display.update()

        clock.tick(24)