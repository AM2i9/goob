import pygame

class Coin:
    def __init__(self):
        self.animation = pygame.transform.scale(
            pygame.image.load("assets/coin.png").convert_alpha(), (512, 64)
        )

        self.frames = [
            self.animation.subsurface(pygame.Rect(64 * i, 0, 64, 64))
            for i in range(0, 8)
        ]

        self.image = self.frames[0]

        self.rect = self.image.get_rect()
        self.state = 0

        self.triggered = False
    
    def check_collision(self, sprite):
        self.triggered = self.rect.colliderect(sprite.rect)
    
    def is_triggered(self):
        return self.triggered

    def draw(self, surface):
        if self.state < 7:
            self.state += 1
        else:
            self.state = 0
        
        self.image = self.frames[self.state]

        surface.blit(self.image, self.rect)
