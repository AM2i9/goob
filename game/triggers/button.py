import pygame
from game.triggers.trigger import Trigger


class Button(Trigger):
    def __init__(self,):
        super().__init__(visible=True)
        self.animation = pygame.transform.scale(
            pygame.image.load("assets/pushthebutton_1.png").convert_alpha(), (320, 126)
        )

        self.frames = [
            self.animation.subsurface(pygame.Rect(64 * i, 0, 64, 42))
            for i in range(0, 5)
        ]

        self.image = self.frames[0]

        self.rect = self.image.get_rect()
        self.state = 0

    def triggered(self):
        if self.state < 4:
            self.state += 1
            self.image = self.frames[self.state]
        super().triggered()

    def untriggered(self):
        if self.state > 0:
            self.state -= 1
            self.image = self.frames[self.state]
        super().untriggered()
