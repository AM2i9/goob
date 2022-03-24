import pygame


class Trigger(pygame.sprite.Sprite):
    """
    A Trigger for another object on the map

    Triggers can be added to those objects, such as traps, and will
    call a method in the object when the Trigger is activated
    """

    def __init__(self, visible: bool = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill((255, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.update(0, 0, 64, 64)
        self.obj = None

        self.visible = visible

    def check_collision(self, sprite):
        if self.rect.colliderect(sprite.hitbox):
            self.triggered()
        else:
            self.untriggered()

    def triggered(self):
        if self.obj:
            self.obj.active()

    def untriggered(self):
        if self.obj:
            self.obj.inactive()

    def add_to_object(self, obj):
        self.obj = obj

    def draw(self, surface):
        surface.blit(self.image, self.rect)
