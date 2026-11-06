import pygame


class Ship:
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # 新飞船方在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        #移动标志（飞船开始不移动）
        self.moving_right = False
        self.moving_left = False

    def update(self):

        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
