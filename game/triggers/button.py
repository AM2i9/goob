import pygame
from game.triggers.trigger import Trigger


class Button(Trigger):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, 18 * 2, 14 * 2, **kwargs)
        self.animation = pygame.transform.scale(pygame.image.load("assets/pushthebutton_1.png").convert_alpha(), (90*3, 42*3))

        self.frames = [
            self.animation.subsurface(pygame.Rect(18 * (3 * i), 0, 18 * 3, 14 * 3))
            for i in range(0, 5)
        ]

        self.image = self.frames[0]
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

