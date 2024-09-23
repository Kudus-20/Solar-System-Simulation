# Author: Abdul-Kudus Alhassan
# Date: 15/02/2023
# Purpose: defining a class to create a body in the solar system

from math import sqrt


class System:
    # the constructor takes a list of bodies
    def __init__(self, body_list):
        self.body_list = body_list

    # this calculates the x and y accelerations of the current body based on all the other bodies in the system
    def compute_acceleration(self, n):  # n is the index of the
        sum_ax = 0  # keeps track of the total x component of acceleration
        sum_ay = 0  # keeps track of the total y component of acceleration
        G = 6.67384e-11  # gravitational constant
        for i in range(len(self.body_list)):
            if i != n:
                dx = self.body_list[i].x - self.body_list[n].x  # x distance between the body and its neighbor
                dy = self.body_list[i].y - self.body_list[n].y  # y distance between the body and its neighbor
                r = sqrt((dx * dx) + (dy * dy))
                a = (G * self.body_list[i].mass) / r ** 2  # calculates the acceleration

                sum_ax += (a * (dx / r))  # updating the x component of the acceleration
                sum_ay += (a * (dy / r))  # updating the  component of the acceleration

        return sum_ax, sum_ay

    def update(self, timestep):
        for i in range(len(self.body_list)):
            self.body_list[i].update_position(timestep)  # updating the position of each body in the system

            ax, ay = self.compute_acceleration(i)  # fetching x and y accelerations
            self.body_list[i].update_velocity(ax, ay, timestep)

    # draws every body in the system
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)
