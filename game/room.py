from typing import Tuple
import pygame
from pygame.locals import SRCALPHA

class Room(pygame.Surface):

    def __init__(self, width: int, height: int, left: int, top: int):
        pygame.Surface.__init__(self, (width, height))
        self.rect = self.get_rect()
        self.rect.update(left, top, width, height)
        
        self.wallmask = pygame.mask.from_surface(pygame.image.load("assets/test_map_2.png"))
        self.walls = self.wallmask.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 255, 255, 150))

    def draw(self, win):
        self.blit(self.walls, self.get_rect())
        win.blit(self, self.rect)