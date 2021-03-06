import sys

import pygame
from pygame.locals import *

from game.room import Room
from game.twin import Twin
from game.menu import Menu

from levels import walk_levels, get_level

import game.wall
import game.coin
import game.level

SPEED = 5


def run_game():
    pygame.init()

    win = pygame.display.set_mode(size=(1280, 720))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Goob")

    pygame.mixer.music.load("assets/music/sb_sundaysmooth.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    room_1 = Room(0)
    room_2 = Room(1)

    levels = walk_levels(room_1, room_2)
    level = next(levels)
    # level = get_level(4, room_1, room_2)

    good_guy = Twin(level.room_1)
    bad_guy = Twin(level.room_2, True)

    x = 0
    y = 0

    level.reset(good_guy, bad_guy)

    Menu().show(win)

    while True:

        if level.is_over():
            try:
                room_1.clear()
                room_2.clear()
                level = next(levels)
                level.reset(good_guy, bad_guy)
            except StopIteration:
                Menu().show(win)
                levels = walk_levels(room_1, room_2)

        if good_guy.is_dead() or bad_guy.is_dead():
            level.reset(good_guy, bad_guy)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    x = SPEED
                elif event.key == K_LEFT:
                    x = -SPEED
                if event.key == K_UP:
                    y = -SPEED
                elif event.key == K_DOWN:
                    y = SPEED
                elif event.key == K_ESCAPE:
                    Menu().show(win)
                    continue
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
