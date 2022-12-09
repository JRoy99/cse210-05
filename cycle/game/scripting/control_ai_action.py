import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlAIAction(Action):
    """
    An input action that controls the bike.
    
    The responsibility of ControlActorsAction is to get the direction and move the bike's bike.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self):
        """Constructs a new ai_action using the specified KeyboardService.
        
        Args:
           
        """
        self._direction = Point(0, -constants.CELL_SIZE)

        

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        bikes = cast.get_actors("bikes")

       
        
        bikes[1].turn_bike(self._direction2)
