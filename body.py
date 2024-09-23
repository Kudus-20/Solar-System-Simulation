# Author: Abdul-Kudus Alhassan
# Date: 15/02/2023
# Purpose: defining a class to create a body in the solar system

from cs1lib import *


class Body:
    # the constructor
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    # this method updates the position of a body using the x and y velocities
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    # this updates the x and y velocities using the component accelerations
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    # this draws the body and colors it
    def draw(self, cx, cy, pixels_per_meter):
        new_x = self.x * pixels_per_meter + cx  # computes the x coordinate of the center of the body
        new_y = self.y * pixels_per_meter + cy  # computes the y coordinate of the center of the body

        set_fill_color(self.r, self.g, self.b)  # color of the body
        set_stroke_color(self.r, self.g, self.b)
        draw_circle(new_x, new_y, self.pixel_radius)  # circular body
