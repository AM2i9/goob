import pygame
from game.traps.trap import Trap


class SpikeTrap(Trap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animation = pygame.transform.scale(
            pygame.image.load("assets/spike-animation.png").convert_alpha(),
            (381, 64),
        )

        self.frames = [
            self.animation.subsurface(pygame.Rect(20, 0, 64, 64)),
            self.animation.subsurface(pygame.Rect(23 + 64, 0, 64, 64)),
            self.animation.subsurface(pygame.Rect(26 + (64 * 2), 0, 64, 64)),
            self.animation.subsurface(pygame.Rect(29 + (64 * 3), 0, 64, 64)),
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
