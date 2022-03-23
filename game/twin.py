import pygame

import game

class Twin(pygame.sprite.Sprite):

    def __init__(self, box):
        pygame.sprite.Sprite.__init__(self)

        self.spritesheet = pygame.transform.scale(pygame.image.load("assets/slime_monster_spritesheet.png").convert_alpha(), (72*2, 72*2))

        self.image = self.spritesheet.subsurface(pygame.Rect(0, 24*4, 24*2, 24*2))

        self.frames = [
            *(self.spritesheet.subsurface(pygame.Rect(24 * (2 * r), 0, 24*2, 24*2))for r in range(3)),
            *(self.spritesheet.subsurface(pygame.Rect(24 * (2 * r), 24*2, 24*2, 24*2))for r in range(3)),
            *(self.spritesheet.subsurface(pygame.Rect(24 * (2 * r), 24*4, 24*2, 24*2))for r in range(3))
        ]

        self.animations = {
            "idle_front": (6, 6, 7, 7, 7, 7, 6, 6,),
            "idle_back": (0, 0, 1, 1, 1, 1, 0, 0, ),
            "idle_side": (3, 3, 4, 4, 4, 4, 3, 3),
            "walk_front": (6, 6, 7, 7, 8, 8),
            "walk_back": (0, 0, 1, 1, 2, 2),
            "walk_side": (3, 3, 4, 4, 5, 5),
        }

        self.dir = 0

        self.rect = self.image.get_rect()

        self.box = box

        self.mask = pygame.mask.from_surface(self.image)

        self.is_dead = False

        self.animate_state = 0;
        self.animation = "idle_front";

    def move(self, x, y):
        self._limit(self.box.get_rect())
        self.rect.move_ip(x, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.check_x_collision(x)

        self.rect.move_ip(0, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.check_y_collision(y)

        if y > 0:
            self.dir = 0
            self.animation = "walk_front"
        elif y < 0:
            self.dir = 3
            self.animation = "walk_back"
        elif x > 0:
            self.dir = 1
            self.animation = "walk_side"
        elif x < 0:
            self.dir = 2
            self.animation = "walk_side"
        else:
            if self.dir == 0:
                self.animation = "idle_front"
            elif self.dir == 1 or self.dir == 2:
                self.animation = "idle_side"
            elif self.dir == 3:
                self.animation = "idle_back"
    
    def check_x_collision(self, x_speed):

        col = self.box.wallmask.overlap_mask(self.mask, (self.rect.x, self.rect.y))
        col_rect = col.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255)).get_bounding_rect()
        dx = col_rect.width
        if dx > 0:
            self.rect.centerx -= dx * (x_speed/game.SPEED)

    def check_y_collision(self, y_speed):
        col = self.box.wallmask.overlap_mask(self.mask, (self.rect.x, self.rect.y))
        col_rect = col.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255)).get_bounding_rect()
        dy = col_rect.height

        if dy > 0:
            self.rect.centery -= dy * (y_speed/game.SPEED)
    
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
    
    def kill(self):
        self.is_dead = True
    
    def draw(self):

        if self.animate_state < len(self.animations[self.animation]) - 1:
            self.animate_state += 1
        else:
            self.animate_state = 0

        self.image = self.frames[self.animations[self.animation][self.animate_state]]

        if self.dir == 2:
            self.image = pygame.transform.flip(self.image, True, False)

        self.box.blit(self.image, self._limit(self.box.get_rect()))