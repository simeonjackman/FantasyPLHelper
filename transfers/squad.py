import json
from typing import Union, List

from .player import Player
from ._autoassign import autoassign


def _random_from_scratch(players: List[Player]):
    """

    """
    return players


def _optimal_from_scratch(players: List[Player],
                          values: List[int]):
    """

    """
    return players


class Squad:
    """

    """

    def __init__(self,
                 players: Union[List[Player], None] = None):
        self.players = players

    @classmethod
    def from_list(cls,
                  squad: List[Player]):
        """

        """
        return cls(squad)

    @classmethod
    def from_dicts(cls,
                   squad: List[dict]):
        """

        """
        squad = [Player.from_dict(p) for p in squad]
        return cls.from_list(squad)

    @classmethod
    def from_json(cls,
                  squad: str):
        """

        """
        squad = json.loads(squad)
        return cls.from_dicts(squad)

    @classmethod
    def random_from_scratch(cls,
                            players: List[Player]):
        """Builds a random team from the list of players.

        """
        squad = _random_from_scratch(players)
        return cls.from_list(squad)

    @classmethod
    def optimal_from_scratch(cls,
                            players: List[Player],
                            values: List[int]):
        """Greedily builds team from scratch while trying to max values.

        """
        squad = _optimal_from_scratch(players, values)
        return cls.from_list(squad)

    def is_valid(self):
        """

        """
        return True

    def is_affordable(self, budget):
        """

        """
        return True
