# PCC (P.285) Ex.14-2 Target Practice.
class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, tp_game):
        """Initialize statistics."""
        self.settings = tp_game.settings
        self.reset_stats()

        # Start Target Practice in an active state.
        self.game_active = True 

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.aliens_left = self.settings.alien_limit
