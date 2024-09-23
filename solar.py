# Author: Abdul-Kudus Alhassan
# Date: 02/15/2023
# Description: Code to simulating the solar system

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6  # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30  # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def main():
    set_clear_color(0, 0, 0)  # black background

    clear()

    # Draw the system in its current state.
    earth_moon.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    earth_moon.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0.2)  # yellow sun
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 2, 1, 1, 0.9)  # grey mercury
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 4, 1, 1, 0.7)  # yellow-white venus
earth = Body(5.9736e24, -149.6e9, 0, 0, 29790, 6, 0.3, 0.3, 1)  # blue earth
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 4, 1, 0, 0)  # red mars

earth_moon = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)
