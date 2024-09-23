# Author: Abdul-Kudus Alhassan
# Date: 15/02/2023
# Purpose: defining a class to create a body in the solar system

from math import sqrt


class System:
    # the constructor takes a list of bodies
    def __init__(self, body_list):
        self.body_list = body_list


    def update(self, timestep):

        for body in self.body_list:
            body.update_position(timestep)

        # for body in self.body_list:
        self.body_list[1].update_velocity(0.0028, 0.0028, timestep)

    # draws every body in the system
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)
