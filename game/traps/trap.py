import pygame

from game.triggers.trigger import Trigger


class Trap(pygame.sprite.Sprite):

    def __init__(self, left: int, top: int, width: int, height: int, trigger: Trigger):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255,0,255))

        self.rect = self.image.get_rect()
        self.rect.update(left, top, width, height)
        self.trigger = trigger
        self.trigger.add_to_object(self)
    
    def active(self):...
    def inactive(self):...