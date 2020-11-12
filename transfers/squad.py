import json
from typing import Union, List

from .player import Player
from ._autoassign import autoassign


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
