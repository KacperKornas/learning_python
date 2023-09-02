import sys
import pygame
from voice import Voice


def check_keydown_events(event, ai_settings, screen, dog, voices):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        dog.moving_right = True
    elif event.key == pygame.K_LEFT:
        dog.moving_left = True
    elif event.key == pygame.K_UP:
        dog.moving_up = True
    elif event.key == pygame.K_DOWN:
        dog.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new voice and add it to the voices group.
        new_voice = Voice(ai_settings, screen, dog)
        voices.add(new_voice)


def check_keyup_events(event, dog):
    """Respond to key releasees."""
    if event.key == pygame.K_RIGHT:
        dog.moving_right = False
    elif event.key == pygame.K_LEFT:
        dog.moving_left = False
    elif event.key == pygame.K_UP:
        dog.moving_up = False
    elif event.key == pygame.K_DOWN:
        dog.moving_down = False

def check_events (ai_settings, screen, dog, voices):
    """Respond to kaypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, dog, voices)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, dog)


def update_screen(ai_settings, screen, dog, voices):
    """Update image to the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    dog.blitme()
    # Redraw all voices behind dog and dogs.
    for voice in voices.sprites():
        voice.draw_voice()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
