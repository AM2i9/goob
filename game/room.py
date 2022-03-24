import pygame
from game.traps.trap import Trap

from game.triggers.trigger import Trigger
from game.wall import Wall


class Room(pygame.Surface):
    def __init__(self, id: int, sprite_startpoint=None):
        pygame.Surface.__init__(self, (576, 640))

        self.rect = self.get_rect()
        self.rect.update((48 if id == 0 else 656, 32), (576, 640))

        self.tiles = []
        self.clear()

        if sprite_startpoint:
            self.sprite_startpoint = sprite_startpoint
    
    def clear(self):
        self.sprite_startpoint = (
                (self.get_width() // 2) - 32,
                (self.get_height() // 2) - 32,
            )
        self.tiles = [[None for _ in range(640 // 64)] for _ in range(576 // 64)]

    def set_tile(self, x, y, tile):
        self.tiles[x][y] = tile

    def draw(self, win, sprite):

        for x, row in enumerate(self.tiles):
            for y, tile in enumerate(row):
                if tile is not None:

                    tile.rect.update(64 * x, 64 * y, tile.rect.width, tile.rect.height)

                    if isinstance(tile, (Trigger, Trap)):
                        tile.check_collision(sprite)

                    tile.draw(self)

        sprite.draw()
        win.blit(self, self.rect)
