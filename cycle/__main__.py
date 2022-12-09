import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.bike import Bike
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("bikes", Bike(.25, .5, constants.GREEN))
    cast.add_actor("bikes", Bike(.75, .5, constants.RED))
    cast.add_actor("scores", Score("Player 1", Point(int(constants.MAX_X * .05), 0), constants.GREEN))
    cast.add_actor("scores", Score("Player 2", Point(int(constants.MAX_X * .8), 0), constants.RED))

   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()