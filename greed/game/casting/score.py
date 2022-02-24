from game.casting.actor import Actor


class Score(Actor):
    """
    Stores and displays current store

    Attributes:
        _points: Points scored
    """
    def __init__(self, points):
        super().__init__()

        self._points = points

    def add_points(self):
        """
        Add 100 points everytime a gem (*) is caught by the user.

        Arg:
            (self): An instance of the Score class.

        Return:
            points: added points
        """
        self._points = self._points + 100

    def deduct_points(self):
        """
        Deduct 100 points everytime a rock (*) is caught by the user.

        Arg:
            (self): An instance of the Score class.

        Return:
            points: added points
        """
        self._points = self._points - 100

    def get_score(self):
        return self._points

    def display_score(self):
        self.set_text(f'Score: {self.get_score()}')