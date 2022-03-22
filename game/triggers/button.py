from game.triggers.trigger import Trigger


class Button(Trigger):
    
    def __init__(self, *args):
        super().__init__(*args, visible=True)