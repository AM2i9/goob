import pygame
from game.traps.trap import Trap

class SpikeTrap(Trap):

    def __init__(self, left, top, *args, **kwargs):
        super().__init__(left, top, 23 * 2, 23 * 2, **kwargs)
        self.animation = pygame.transform.scale(pygame.image.load("assets/spike-animation.png").convert_alpha(), (125*2, 21*2))

        self.frames = [
            self.animation.subsurface(pygame.Rect(10, 0, 23 * 2, 21 * 2)),
            self.animation.subsurface(pygame.Rect(10 + (22 * 2), 0, 23 * 2, 21 * 2)),
            self.animation.subsurface(pygame.Rect(10 + (22 * 4), 0, 23 * 2, 21 * 2)),
            self.animation.subsurface(pygame.Rect(10 + (22 * 6), 0, 23 * 2, 21 * 2)),
        ]

        self.image = self.frames[0]

        self.shown = True
        self.state = 0

    def active(self):
        if self.state < 3:
            self.state += 1
            self.image = self.frames[self.state]

    def inactive(self):
        if self.state > 0:
            self.state -= 1
            self.image = self.frames[self.state]
    
    def kill_sprite(self, sprite):
        if self.state > 2:
            sprite.kill()