

class BaseScoreFunction(object):
    """Base class for all score functions.

    """

    def __init__(self):
        pass

    def __call__(self):
        """Must be overwritten!

        """
        raise NotImplementedError()
