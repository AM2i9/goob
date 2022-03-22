import pygame

class Trigger(pygame.sprite.Sprite):
    """
    A Trigger for another object on the map

    Triggers can be added to those objects, such as traps, and will
    call a method in the object when the Trigger is activated
    """

    def __init__(self, left: int, top: int, width: int, height: int, visible: bool = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255,0,255))

        self.rect = self.image.get_rect()
        self.rect.update(left, top, width, height)
        self.obj = None

        self.visible = visible
    
    def check_collision(self, sprite):
        if pygame.sprite.collide_rect(self, sprite):
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