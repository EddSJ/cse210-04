from game.casting.actor import Actor

class Gem(Actor):
    """
    A gem (*) that the user will try to catch. 
    
    The responsibility of a Gem is to provide something for the user to earn
    points catching.

    Attributes:
        None
    """
    def __init__(self):
        super().__init__()

    def update_score(self, score):
        """
        Add 100 points everytime a gem (*) is caught by the user.

        Arg:
            (self): An instance of the Gem class.

        Return:
            points: added points
        """
        score.add_points()