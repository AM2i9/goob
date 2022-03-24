import pygame

from game.triggers.trigger import Trigger


class Trap(pygame.sprite.Sprite):
    def __init__(self, trigger: Trigger):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill((255, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.update(0, 0, 64, 64)
        self.trigger = trigger
        self.trigger.add_to_object(self)

        self.shown = False

    def active(self):
        ...

    def inactive(self):
        ...

    def kill_sprite(self, sprite):
        ...

    def check_collision(self, sprite):
        if self.rect.colliderect(sprite.hitbox):
            self.kill_sprite(sprite)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
