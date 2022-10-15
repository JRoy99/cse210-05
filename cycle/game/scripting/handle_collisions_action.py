import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the bike collides
    with the food, or the bike collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the bike collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        bikes = cast.get_actors("bikes")
        scores = cast.get_actors("scores")
        bike1 = bikes[0].get_segments()[0]
        bike2 = bikes[1].get_segments()[0]
        segments1 = bikes[0].get_segments()[1:]
        segments2 = bikes[1].get_segments()[1:]
        
        for segment in segments1:
            if bike1.get_position().equals(segment.get_position()):
                scores[0].add_points(-1)
                if scores[0]._points == 0:
                    self._is_game_over = True
                    self.winner = "Player 2"
            if bike2.get_position().equals(segment.get_position()):
                scores[1].add_points(-1)
                if scores[1]._points == 0:
                    self._is_game_over = True
                    self.winner = "Player 1"
        for segment in segments2:
            if bike1.get_position().equals(segment.get_position()):
                scores[0].add_points(-1)
                if scores[0]._points == 0:
                    self._is_game_over = True
                    self.winner = "Player 2"
            if bike2.get_position().equals(segment.get_position()):
                scores[1].add_points(-1)
                if scores[1]._points == 0:
                    self._is_game_over = True
                    self.winner = "Player 1"
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the bike and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            bikes = cast.get_actors("bikes")
            segments1 = bikes[0].get_segments()
            segments2 = bikes[1].get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)

            position = Point(x, y-150)
            message_gameover = Actor()
            message_gameover.set_text("Game Over!") 
            message_gameover.set_font_size(5*constants.FONT_SIZE)
            message_gameover.set_position(position)
            cast.add_actor("messages", message_gameover)
          
            position = Point(x, y-50)
            message_winner = Actor()
            message_winner.set_text(f"{self.winner} wins!")
            message_winner.set_font_size(3*constants.FONT_SIZE)
            message_winner.set_position(position)
            cast.add_actor("messages", message_winner)

            for bike in bikes:
                bike.set_color(constants.WHITE)
            for segment in segments1:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)