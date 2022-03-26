import pygame

from typing import List, Tuple
from dataclasses import dataclass
from game.coin import Coin

from game.room import Room
from game.traps import TRAPS
from game.triggers import TRIGGERS


@dataclass
class Level:

    id: int

    room_1: Room
    room_2: Room

    end_coin: Coin

    def __post_init__(self):
        self.font = pygame.font.Font("assets/MisterPixelRegular.otf", 64)
        self.level_num_text = self.font.render(f"{self.id}", 8, (255, 255, 255))

    def reset(self, good_twin, evil_twin):
        good_twin.rect.update(
            *self.room_1.sprite_startpoint, good_twin.rect.width, good_twin.rect.height
        )
        evil_twin.rect.update(
            *self.room_2.sprite_startpoint, evil_twin.rect.width, evil_twin.rect.height
        )
        good_twin.dead = False
        evil_twin.dead = False

    def draw(self, win, good_twin, evil_twin):
        self.end_coin.check_collision(good_twin)

        self.room_1.fill((64, 77, 88))
        self.room_2.fill((88, 64, 64))

        self.room_1.draw(win, good_twin)
        self.room_2.draw(win, evil_twin)

        win.blit(self.level_num_text, self.level_num_text.get_rect().move(12, 32))

    def is_over(self) -> bool:
        return self.end_coin.is_triggered()
