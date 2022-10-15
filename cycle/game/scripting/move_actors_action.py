from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 
class MoveActorsAction(Action):
    """
    An update action that handles actor movement.
    
    The responsibility of MoveActorsAction is to iterate through all move_next() methods for actors. 
    """
    def execute(self, cast, script):
        """Executes move_next() method for all actors

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()

        for i in actors:
            i.move_next()

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor