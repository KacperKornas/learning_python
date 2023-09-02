import sys
import pygame
from pygame.sprite import Group


from settings import Settings
from dog import Dog
import game_function as gf


def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Maltese Invasion")

    # Make a dog.
    dog = Dog(ai_settings, screen)
    # Make a group to store bullets in.
    voices = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, dog, voices)
        dog.update()
        voices.update()
        gf.update_screen(ai_settings, screen, dog, voices)


run_game()
