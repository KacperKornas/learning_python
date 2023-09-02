import pygame
from pygame.sprite import Sprite


class Voice(Sprite):
    """A class to manage dog barking."""

    def __init__(self, ai_settings, screen, dog):
        """Create a voice object at the dog's current position."""
        super(Voice, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.voice_width,
            ai_settings.voice_height)
        self.rect.centerx = dog.rect.centerx
        self.rect.top = dog.rect.top

        # Store the bullet;s position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.voice_color
        self.speed_factor = ai_settings.voice_speed_factor

    def update(self):
        """Move the voice up the screen."""
        # Update the decimal position of the voice.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_voice(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
