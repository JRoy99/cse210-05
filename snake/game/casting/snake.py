import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        
    """
    def __init__(self, x_mod, y_mod, dir, def_color):
        super().__init__()
        self._segments = []
        self._prepare_body(x_mod, y_mod, dir)
        self._color = def_color

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

        self.grow_tail(1)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, x_mod, y_mod, dir):
        x = int(constants.MAX_X * x_mod)
        y = int(constants.MAX_Y * y_mod)

        position = Point(x, y * constants.CELL_SIZE)
        if dir == 'u':
            velocity = Point(0, 1 * -constants.CELL_SIZE)
        elif dir == 'd':
            velocity = Point(0, -1 * -constants.CELL_SIZE)
        text = "8"
            
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(self._color)
        self._segments.append(segment)