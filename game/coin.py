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
        self.pos_state = 0

        self.triggered = False
    
    def check_collision(self, sprite):
        if self.rect.colliderect(sprite.rect):
            self.triggered = True
    
    def is_triggered(self):
        return self.triggered and self.pos_state > 25

    def draw(self, surface):
        if self.state < 7:
            self.state += 1
        else:
            self.state = 0

        if self.triggered:
            self.rect.move_ip(0, 0.25 * (self.pos_state - 10) ** 2 - 25)
            self.pos_state += 1
        
        self.image = self.frames[self.state]

        surface.blit(self.image, self.rect)
