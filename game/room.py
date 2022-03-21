from typing import Tuple
import pygame

class Room(pygame.Surface):

    def __init__(self, width: int, height: int, left: int, top: int):
        pygame.Surface.__init__(self, (width, height))
        self.rect = self.get_rect()
        self.rect.update(left, top, width, height)
    
    def draw(self, win):
        win.blit(self, self.rect)