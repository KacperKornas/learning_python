import pygame

class Rocket:


    def __init__(self, g_settings, window):

        self.window = window
        self.g_settings = g_settings

        self.rocket = pygame.image.load('images/rocket.png')
        self.rect = self.rocket.get_rect()
        self.window_rect = window.get_rect()

        self.rect.centerx = self.window_rect.centerx
        self.rect.centery = self.window_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):

        if self.moving_right and self.rect.right < self.window_rect.right:
            self.centerx += self.g_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.g_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.window_rect.bottom:
            self.centery += self.g_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.g_settings.rocket_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.window.blit(self.rocket, self.rect)
