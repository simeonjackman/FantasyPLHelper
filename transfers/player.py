import copy
from typing import Union

from ._autoassign import autoassign


def _parse_argument(s):
    """

    """
    if s is None:
        return s
    if isinstance(s, int):
        return s
    if isinstance(s, float):
        return s
    try:
        return str(s)
    except Exception:
        return s


class Player:
    """

    """

    def __init__(self,
                 chance_of_playing_next_round: Union[int, None] = None,
                 chance_of_playing_this_round: Union[int, None] = None,
                 code: Union[int, None] = None,
                 cost_change_event: Union[int, None] = None,
                 cost_change_event_fall: Union[int, None] = None,
                 cost_change_start: Union[int, None] = None,
                 cost_change_start_fall: Union[int, None] = None,
                 dreamteam_count: Union[int, None] = None,
                 element_type: Union[int, None] = None,
                 ep_next: Union[float, None] = None,
                 ep_this: Union[float, None] = None,
                 event_points: Union[int, None] = None,
                 first_name: Union[str, None] = None,
                 form: Union[float, None] = None,
                 id: Union[int, None] = None,
                 in_dreamteam: Union[bool, None] = None,
                 news: Union[str, None] = None,
                 news_added: Union[str, None] = None,
                 now_cost: Union[int, None] = None,
                 photo: Union[str, None] = None,
                 points_per_game: Union[float, None] = None,
                 second_name: Union[str, None] = None,
                 selected_by_percent: Union[str, None] = None,
                 special: Union[bool, None] = None,
                 squad_number: Union[str, None] = None,
                 status: Union[str, None] = None,
                 team: Union[int, None] = None,
                 team_code: Union[int, None] = None,
                 total_points: Union[int, None] = None,
                 transfers_in: Union[int, None] = None,
                 transfers_in_event: Union[int, None] = None,
                 transfers_out: Union[int, None] = None,
                 transfers_out_event: Union[int, None] = None,
                 value_form: Union[float, None] = None,
                 value_season: Union[float, None] = None,
                 web_name: Union[str, None] = None,
                 minutes: Union[int, None] = None,
                 goals_scored: Union[int, None] = None,
                 assists: Union[int, None] = None,
                 clean_sheets: Union[int, None] = None,
                 goals_conceded: Union[int, None] = None,
                 own_goals: Union[int, None] = None,
                 penalties_saved: Union[int, None] = None,
                 penalties_missed: Union[int, None] = None,
                 yellow_cards: Union[int, None] = None,
                 red_cards: Union[int, None] = None,
                 saves: Union[int, None] = None,
                 bonus: Union[int, None] = None,
                 bps: Union[int, None] = None,
                 influence: Union[float, None] = None,
                 creativity: Union[float, None] = None,
                 threat: Union[float, None] = None,
                 ict_index: Union[float, None] = None,
                 influence_rank: Union[int, None] = None,
                 influence_rank_type: Union[int, None] = None,
                 creativity_rank: Union[int, None] = None,
                 creativity_rank_type: Union[int, None] = None,
                 threat_rank: Union[int, None] = None,
                 threat_rank_type: Union[int, None] = None,
                 ict_index_rank: Union[int, None] = None,
                 ict_index_rank_type: Union[int, None] = None,
                 corners_and_indirect_freekicks_order: Union[int, None] = None,
                 corners_and_indirect_freekicks_text: Union[str, None] = None,
                 direct_freekicks_order: Union[int, None] = None,
                 direct_freekicks_text: Union[str, None] = None,
                 penalties_order: Union[int, None] = None,
                 penalties_text: Union[str, None] = None):
        # autoassign above attributes
        autoassign(locals())

    @classmethod
    def from_dict(cls, player_dict):
        """

        """
        player_dict_copy = copy.deepcopy(player_dict)
        for key, item in player_dict_copy.items():
            player_dict_copy[key] = _parse_argument(item)
        return cls(**player_dict_copy)