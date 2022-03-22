import pygame

class Twin(pygame.sprite.Sprite):

    def __init__(self, box):
        pygame.sprite.Sprite.__init__(self)

        self.surface = pygame.Surface((30, 30))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()

        self.box = box

        self.mask = pygame.mask.from_surface(self.surface)

    def move(self, x, y):
        self._limit(self.box.get_rect())
        self.rect.move_ip(x, 0)
        self.mask = pygame.mask.from_surface(self.surface)
        self.check_x_collision(x)

        self.rect.move_ip(0, y)
        self.mask = pygame.mask.from_surface(self.surface)
        self.check_y_collision(y)
    
    def check_x_collision(self, x_speed):

        col = self.box.wallmask.overlap_mask(self.mask, (self.rect.x, self.rect.y))
        col_rect = col.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255)).get_bounding_rect()
        dx = col_rect.width
        if dx > 0:
            self.rect.centerx -= dx * (x_speed/10)

    def check_y_collision(self, y_speed):
        col = self.box.wallmask.overlap_mask(self.mask, (self.rect.x, self.rect.y))
        col_rect = col.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255)).get_bounding_rect()
        dy = col_rect.height

        if dy > 0:
            self.rect.centery -= dy * (y_speed/10)
    
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