import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx  # Every ship spawns at the center of the screen
        self.rect.bottom = self.screen_rect.bottom  # Every ship spawns at the bottom of the screen
        self.center = float(self.rect.centerx)
        self.moving_right = False  # Ship right side movement
        self.moving_left = False  # Ship left side movement

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        # Displaying ship in his actual position
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
