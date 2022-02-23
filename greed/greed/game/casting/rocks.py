from game.casting.actor import Actor


class Rock(Actor):
    """
    A rock (o) that the user will try to avoid. 
    
    The responsibility of a Rock is to provide something for the user to try
    to avoid and to loose points if caught.

    Attributes:
        _points (0): points lost by accidentally catching rocks.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        
    def subract_points(self):
        """
        Subract 100 points everytime a rock (o) is caught by the user.

        Arg:
            (self): An instance of the Rock class.

        Return:
            points: subracted points
        """
        self._points -= 100
        return self._points