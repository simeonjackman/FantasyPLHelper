from dataloader.scores._base import BaseScoreFunction

class ScorerPointsScoreFunction(BaseScoreFunction):
    """Dummy score function which returns the sum of assists and scored goals.

    """

    def __init__(self):
        super(ScorerPointsScoreFunction, self).__init__()
        self.__name__ = 'scorer_points'

    def __call__(self, player: dict):
        """Returns the score function for the given player.

        Args:
            player:
                Dictionary containing data about the player.
        
        Returns:
            The number of scorer points of the player in the current season.

        """
        return player['assists'] + player['goals_scored']