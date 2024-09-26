class Settings:
    """存储游戏《外星人》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.5
        # 飞船生命限制
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 最大子弹限制
        self.bullets_allowed = 3
        # 外星人移速
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # 外星人移动方向 1为向右移动 -1为向左移动
        self.fleet_direction = 1
