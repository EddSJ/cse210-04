from game.casting.actor import Actor


class Gem(Actor):
    """
    A gem (*) that the user will try to catch. 
    
    The responsibility of a Gem is to provide something for the user to earn
    points catching.

    Attributes:
        _points (100): points earned by getting gems.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def add_points(self):
        """
        Add 100 points everytime a gem (*) is caught by the user.

        Arg:
            (self): An instance of the Gem class.

        Return:
            points: added points
        """
        return self._points + 100