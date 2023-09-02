import pygame

class Settings:

    def __init__(self):


        self.width = 1200
        self.height = 800
        self.rocket_speed_factor = 0.2
        self.bg_img = pygame.image.load('images/bg.webp')
        self.bg_img = pygame.transform.scale(self.bg_img,(self.width,self.height))

