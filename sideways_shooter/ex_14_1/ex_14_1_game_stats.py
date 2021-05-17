# Sideways Shooter pt.2. Bring this up to Alien Invasion level. Sideways movement, etc.
class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()

        # Start Sideways Shooter in an active state.
        self.game_active = True 

    def reset_stats(self):
        """Initialize statistics taht can change during the game."""
        self.ships_left = self.settings.ship_limit
