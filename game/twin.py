import pygame

class Twin(pygame.sprite.Sprite):

    def __init__(self, box):
        pygame.sprite.Sprite.__init__(self)

        self.surface = pygame.Surface((30, 30))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()

        self.box = box 

    def move(self, x, y):
        self._limit(self.box.get_rect())
        self.rect.move_ip(x, y)
    
    
    def _limit(self, rect):
        if self.rect.x < rect.left:
            self.rect.x = rect.left
        if self.rect.x > rect.right:
            self.rect.x = rect.right
        if self.rect.y < rect.top:
            self.rect.y = rect.top
        if self.rect.y > rect.bottom:
            self.rect.y = rect.bottom

        return self.rect.clamp(rect)
    
    def draw(self):
        self.box.blit(self.surface, self._limit(self.box.get_rect()))