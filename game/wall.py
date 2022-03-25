import pygame


class WallType:
    VERTICAL = 0
    HORIZONTAL = 1
    FOURWAY = 2
    L_TJUNCT = 3
    D_TJUNCT = 4
    R_TJUNCT = 5
    U_TJUNCT = 6
    UR_LJUNCT = 7
    UL_LJUNCT = 8
    DL_LJUNCT = 9
    DR_LJUNCT = 10
    HORIZONTAL_LEFT_END = 11
    VERTICAL_TOP_END = 12
    HORIZONTAL_RIGHT_END = 13
    VERTICAL_BOTTOM_END = 14
    SINGLE = 15

    @staticmethod
    def get_wall(type: int):
        walls_raw = pygame.transform.scale(
            pygame.image.load("assets/walls.png").convert_alpha(), (960, 64)
        )

        if type == WallType.SINGLE:
            return pygame.transform.scale(
                pygame.image.load("assets/default_tiles_x.png").convert_alpha(),
                (512, 128),
            ).subsurface((64, 0, 64, 64))

        return walls_raw.subsurface((64 * type, 0, 64, 64))


class Wall(pygame.sprite.Sprite):
    def __init__(self, type: WallType):
        pygame.sprite.Sprite.__init__(self)

        self.image = WallType.get_wall(type)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
