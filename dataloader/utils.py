import re
from typing import Union

def str2bool(v: Union[str, bool]) -> str:
    """Convert a string to boolean

    """
    if isinstance(v, bool):
        return v
    if v.lower() in ['yes', 'true', 't', 'y', '1']:
        return True
    if v.lower() in ['no', 'false', 'f', 'n', '0']:
        return False
    return True


# any date in the 2000s will do
DATE_EXP = '2[0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]T'
# time from 00:00:00Z to 24:00:00Z
TIME_EXP = '[0-2][0-9]:[0-5][0-9]:[0-5][0-9]Z'


def correct_time_format(fmt: str) -> bool:
    """Check whether the deadline time has the right format

    Correct format and example:
        YYYY-MM-DDTHH:MM:SS
        2020-10-18T12:00:00

    """
    exp = DATE_EXP + TIME_EXP
    if re.search(exp, fmt) is not None:
        return True
    else:
        return False
