import pygame
from game.traps.trap import Trap

from game.triggers.trigger import Trigger
from game.wall import Wall


class Room(pygame.Surface):
    def __init__(self, id: int, sprite_startpoint=None):
        pygame.Surface.__init__(self, (576, 640))

        self.rect = self.get_rect()
        self.rect.update((32 + 16 if id == 0 else 640 + 16, 32), (576, 640))

        self.tiles = [[None for _ in range(576 // 64)] for _ in range(576 // 64)]

        if sprite_startpoint is None:
            self.sprite_startpoint = (
                (self.get_width() // 2) - 15,
                (self.get_height() // 2) - 15,
            )

    def add_trap(self, trap):
        ...

    def add_trigger(self, trigger):
        ...

    def set_tile(self, x, y, tile):
        self.tiles[x][y] = tile

    def draw(self, win, sprite):

        for x, row in enumerate(self.tiles):
            for y, tile in enumerate(row):
                if tile is not None:

                    tile.update(64 * x, 64 * y)

                    if isinstance(tile, (Trigger, Trap)):
                        tile.check_collision(sprite)

                    tile.draw(self)

        sprite.draw()
        win.blit(self, self.rect)
