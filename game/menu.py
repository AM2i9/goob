import pygame
from pygame.locals import *

class Menu(pygame.Surface):

    def __init__(self):
        super().__init__((1280, 720))

        self.rect = self.get_rect()

        self.font = pygame.font.Font("assets/MisterPixelRegular.otf", 64)

    def show(self, win):

        title = self.font.render("<Insert Name Here>", 8, (255, 255, 255))

        play = pygame.transform.scale(self.font.render("Play", 8, (249, 240, 107)), (96+16, 48))
        play_unselected = pygame.transform.scale(self.font.render("Play", 8, (222, 221, 218)), (96+16, 48))
        credits = pygame.transform.scale(self.font.render("Credits", 8, (249, 240, 107)), (176, 48))
        credits_unselected = pygame.transform.scale(self.font.render("Credits", 8, (222, 221, 218)), (176, 48))

        selected = 0

        while selected != 2:

            self.blit(title, title.get_rect().move(32, 32))

            if selected == 0:
                self.blit(play, play.get_rect().move(32, 96))
                self.blit(credits_unselected, credits_unselected.get_rect().move(32, 96+64))
            elif selected == 1:
                self.blit(play_unselected, play.get_rect().move(32, 96))
                self.blit(credits, credits_unselected.get_rect().move(32, 96+64))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        selected = 0
                    elif event.key == K_DOWN:
                        selected = 1
                    elif event.key == K_RETURN:
                        if selected == 0:
                            selected = 2
                        else:
                            selected = 3

            win.blit(self, self.get_rect())

            pygame.display.update()