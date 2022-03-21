import pygame
from pygame.locals import *
from game.room import Room

from game.twin import Twin

def run_game():
    pygame.init()

    win = pygame.display.set_mode(size=(1280, 720))
    clock = pygame.time.Clock()

    box_1 = Room(595, 660, 30, 30)
    box_2 = Room(595, 660, 655, 30)

    good_guy = Twin(box_1)
    bad_guy = Twin(box_2)

    x = 0
    y = 0

    good_guy.move((box_1.get_width() // 2) - 15, (box_1.get_height() // 2) - 15)
    bad_guy.move((box_2.get_width() // 2) - 15, (box_2.get_height() // 2) - 15)

    while True:
        
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

        box_1.fill((64, 77, 88))
        box_2.fill((88, 64, 64))

        good_guy.draw()
        bad_guy.draw()

        box_1.draw(win)
        box_2.draw(win)

        pygame.display.update()

        clock.tick(24)