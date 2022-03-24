import pygame

import game
from game.wall import Wall


class Twin(pygame.sprite.Sprite):
    def __init__(self, box, blue: bool = False):
        pygame.sprite.Sprite.__init__(self)

        self.spritesheet = pygame.transform.scale(
            pygame.image.load("assets/slime_monster_spritesheet.png").convert_alpha(),
            (192, 192),
        )

        if blue:
            w, h = self.spritesheet.get_size()
            for r in range(w):
                for c in range(h):
                    color = self.spritesheet.get_at((r, c))
                    if color[3] > 0:
                        self.spritesheet.set_at(
                            (r, c), (color[2], color[1], color[0], 255)
                        )

        self.frames = [
            *(
                self.spritesheet.subsurface(pygame.Rect(64 * r, 0, 64, 64))
                for r in range(3)
            ),
            *(
                self.spritesheet.subsurface(pygame.Rect(64 * r, 64, 64, 64))
                for r in range(3)
            ),
            *(
                self.spritesheet.subsurface(pygame.Rect(64 * r, 64 * 2, 64, 64))
                for r in range(3)
            ),
        ]

        self.image = self.frames[0]

        self.animations = {
            "idle_front": (
                6,
                6,
                7,
                7,
                7,
                7,
                6,
                6,
            ),
            "idle_back": (
                0,
                0,
                1,
                1,
                1,
                1,
                0,
                0,
            ),
            "idle_side": (3, 3, 4, 4, 4, 4, 3, 3),
            "walk_front": (6, 6, 7, 7, 8, 8),
            "walk_back": (0, 0, 1, 1, 2, 2),
            "walk_side": (3, 3, 4, 4, 5, 5),
        }

        self.dir = 0

        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width // 2, self.rect.height // 2
        )

        self.box = box

        self.mask = pygame.mask.from_surface(self.image)

        self.dead = False
        self.death_anim_state = 0

        self.animate_state = 0
        self.animation = "idle_front"

    def move(self, x, y):
        if not self.dead:
            self.rect.move_ip(x, 0)
            for row in self.box.tiles:
                for tile in row:
                    if isinstance(tile, Wall):
                        self.check_x_collision(tile, x)

            self.rect.move_ip(0, y)
            for row in self.box.tiles:
                for tile in row:
                    if isinstance(tile, Wall):
                        self.check_y_collision(tile, y)

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

    def check_x_collision(self, tile, x_speed):
        col = tile.mask.overlap_mask(self.mask, (self.rect.x-tile.rect.x, self.rect.y-tile.rect.y))
        col_rect = col.to_surface(
            unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255)
        ).get_bounding_rect()
        dx = col_rect.width
        if dx > 0:
            self.rect.centerx -= dx * (x_speed / game.SPEED)

    def check_y_collision(self, tile, y_speed):
        col = tile.mask.overlap_mask(self.mask, (self.rect.x-tile.rect.x, self.rect.y-tile.rect.y))
        col_rect = col.to_surface(
            unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255)
        ).get_bounding_rect()
        dy = col_rect.height
        if dy > 0:
            self.rect.centery -= dy * (y_speed / game.SPEED)

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
        self.dead = True

    def is_dead(self) -> bool:

        return self.dead and self.death_anim_state > 25

    def draw(self):

        if self.animate_state < len(self.animations[self.animation]) - 1:
            self.animate_state += 1
        else:
            self.animate_state = 0

        if self.dead:
            self.animate_state = 0
            self.death_anim_state += 1

        self.image = self.frames[self.animations[self.animation][self.animate_state]]

        if self.dir == 2:
            self.image = pygame.transform.flip(self.image, True, False)

        self.hitbox.update(
            self.rect.x + self.image.get_width() // 4,
            self.rect.y + self.image.get_height() // 4,
            self.image.get_width() // 2,
            self.image.get_height() // 2,
        )

        self.box.blit(self.image, self._limit(self.box.get_rect()))
