import pygame
from pygame.locals import *

class Menu(pygame.Surface):

    def __init__(self):
        super().__init__((1280, 720))

        self.rect = self.get_rect()

        self.font = pygame.font.Font("assets/MisterPixelRegular.otf", 64)

    def show(self, win):

        title = self.font.render("<Insert Name Here>", 8, (255, 255, 255))

        play = pygame.transform.scale(self.font.render("Press ENTER to play", 8, (249, 240, 107)), (512, 48))

        info_1 = pygame.transform.scale(self.font.render("https://github.com/AM2i9", 8, (255, 255, 255)), (320, 32))
        info_2 = pygame.transform.scale(self.font.render("Created for Pyweek 33", 8, (255, 255, 255)), (320, 32))

        slime_thing = pygame.transform.scale(
            pygame.image.load("assets/slime_monster_spritesheet.png").convert_alpha(),
            (1536, 1536),
        ).subsurface((0, 512*2, 512, 512))

        while True:

            self.blit(title, title.get_rect().move(32, 32))

            self.blit(play, play.get_rect().move(32, 96))

            self.blit(info_2, info_2.get_rect().move(32, 610))
            self.blit(info_1, info_1.get_rect().move(32, 650))

            self.blit(slime_thing, slime_thing.get_rect().move(640, 240))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        return

            win.blit(self, self.get_rect())

            pygame.display.update()