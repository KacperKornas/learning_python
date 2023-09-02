class Settings:
    """A class to store all settings for Maltese Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 159, 104)

        # Dog settings
        self.dog_speed_factor = 0.2

        # Voice settings
        self.voice_speed_factor = 0.4
        self.voice_width = 20
        self.voice_height = 10
        self.voice_color = 60, 60, 60
