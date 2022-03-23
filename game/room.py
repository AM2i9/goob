import pygame

class Room(pygame.Surface):

    def __init__(self, id: int, walls: str, sprite_startpoint = None):
        pygame.Surface.__init__(self, (595, 660))
        self.rect = self.get_rect()
        self.rect.update((30 if id == 0 else 655, 30), (595, 660))
        
        self.walls_file = walls
        self.wallmask = pygame.mask.from_surface(pygame.image.load(walls))
        self.walls = self.wallmask.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 255, 255, 150))

        self.traps = []
        self.triggers = []

        self.sprite_startpoint = sprite_startpoint
        if sprite_startpoint is None:
            self.sprite_startpoint = ((self.get_width() // 2) - 15, (self.get_height() // 2) - 15)

    def add_trap(self, trap):
        self.traps.append(trap)

    def add_traps(self, traps):
        for trap in traps:
            self.add_trap(trap)

    def add_trigger(self, trigger):
        self.triggers.append(trigger)
    
    def add_triggers(self, triggers):
        for trigger in triggers:
            self.add_trap(trigger)

    def draw(self, win, sprite):

        for trap in self.traps:
            trap.check_collision(sprite)
            if trap.shown:
                trap.draw(self)
        
        for trigger in self.triggers:
            trigger.check_collision(sprite)
            if trigger.visible:
                trigger.draw(self)
        
        sprite.draw()

        self.blit(self.walls, self.get_rect())
        win.blit(self, self.rect)
    
    def to_dict(self):
        data = {
            "sprite_startpoint": self.sprite_startpoint,
            "walls": self.walls_file,
        }
        data["traps"] = [
            {
                "type": trap.__class__.__name__,
                "left": trap.rect.left,
                "top": trap.rect.top,
                "width": trap.rect.width,
                "height": trap.rect.height,
                "shown_default": trap.shown,
                "trigger": {
                    "type": trap.trigger.__class__.__name__,
                    "in_room": trap.trigger in self.triggers,
                    "left": trap.trigger.rect.left,
                    "top": trap.trigger.rect.top,
                    "width": trap.trigger.rect.width,
                    "height": trap.trigger.rect.height,
                    "visible_default": trap.trigger.visible,
                }
            } for trap in self.traps
        ]
        return data
    
    @classmethod
    def from_dict(cls, data, id):
        return cls(
            id=id,
            walls=data["walls"],
            sprite_startpoint=data["sprite_startpoint"]
        )

