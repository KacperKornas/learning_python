import sys
import pygame

from settings import Settings
from rocket import Rocket
import game_function as gf

def run_game():

    pygame.init()
    g_settings = Settings()
    window = pygame.display.set_mode(
        (g_settings.width, g_settings.height))
    pygame.display.set_caption("Rocket Game")

    rocket = Rocket(g_settings, window)

    while True:

        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(g_settings, window, rocket)

run_game()



