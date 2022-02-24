import random

from game.casting.actor import Actor
from game.casting.gems import Gem
from game.casting.rocks import Rock
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

# This is the starting score
STARTING_SCORE = 500

def main():
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Score(STARTING_SCORE)
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)
    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the gems and rocks
    for n in range(DEFAULT_ARTIFACTS):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # randomly select this to be either a gem or a rock
        if random.randint(1, 2) == 1:
            artifact = Gem()
            artifact.set_text("*")
        else:
            artifact = Rock()
            artifact.set_text("o")

        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)
        
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()