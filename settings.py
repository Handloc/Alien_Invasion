class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (38, 38, 38)
        # Ship
        self.ship_limit = 3
        # Bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 68
        self.bullets_allowed = 3
        # Alien
        self.fleet_drop_speed = 10
        # Game speed
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.85
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale * 0.7
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale