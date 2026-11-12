class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed = 8
        self.ship_limit = 3

        #子弹
        self.bullet_speed = 5.0
        self.bullet_width = 2
        self.bullet_height = 8
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # fleet_direction 1 表示右移，-1表示左移动
        self.fleet_direction = 1
