from game.traps.trap import Trap

class SpikeTrap(Trap):

    def __init__(self, surface, *args):
        super().__init__(*args)
        self.surface = surface

    def active(self):
        print("test")
        self.surface.blit(self.image, self.rect)