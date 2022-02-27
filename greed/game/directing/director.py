import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._counter = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        self._counter = self._counter + 1

        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.display_score()
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        if self._counter == 5:

            for artifact in artifacts:
                position_1 = random.randint(20, 40)
                position_2 = random.randint(20, 40)
                position_3 = random.randint(20, 40)
                position_4 = random.randint(20, 40)
                artifact.position = artifact.get_position()
                artifact.position._y = (artifact.position._y + 15) % max_y
                artifact.set_velocity(100)
                artifact.position._x = (artifact.position._x + position_1 ) % max_x
                artifact.position._x = (artifact.position._x + position_2 ) % max_x
                artifact.position._x = (artifact.position._x - position_3 ) % max_x
                artifact.position._x = (artifact.position._x - position_4 ) % max_x

                if robot.get_position().equals(artifact.get_position()):
                    artifact.update_score(banner)

                    banner.display_score()
            self._counter = 0
      
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()