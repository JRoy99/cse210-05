import constants
from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by forcing a collision.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, text, position, color):
        super().__init__()
        self._points = 0
        self._text1 = text
        self.set_position(position)
        self.set_font_size(constants.FONT_SIZE*2)
        self.set_color(color)
        self.set_text(f"{self._text1}")