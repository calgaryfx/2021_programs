# PCC (P.285) Ex.14-2 Target Practice.
class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.shots_left = self.settings.missed_shots
