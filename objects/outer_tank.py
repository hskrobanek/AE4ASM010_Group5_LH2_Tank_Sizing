import numpy as np
import matplotlib.pyplot as plt

from cryotank_sizing.tank_general_properties import tank_height, get_tank_volume

class OuterTank:
    def __init__ (self, fuselage, inner_tank):
        self.inner_tank = inner_tank
        self.fuselage = fuselage

    def get_outer_tank_dimensions(self):

        # Apply offset to the inner tank dimensions
        r_outer = self.inner_tank.get_inner_tank_dimensions()[0] + self.inner_tank.offset
        l_outer = self.inner_tank.get_inner_tank_dimensions()[1] + 2* self.inner_tank.offset

        # Calculate the volume and return the result
        volume_outer = get_tank_volume(r_outer, l_outer)

        self.outer_dimensions = [r_outer, l_outer, volume_outer]

        return self.outer_dimensions

class FitCheck:
    def __init__ (self, fuselage, innertank, outertank):
        self.fuselage = fuselage
        self.innertank = innertank
        self.outertank = outertank


    def check_if_outer_tank_fits(self):
        outer_dimensions = self.outertank.get_outer_tank_dimensions()
        fuselage_heights = self.fuselage.fuselage_height

        tank_length_partial = outer_dimensions[0] * 0.75 + outer_dimensions[1]
        tank_length_full = tank_length_partial + outer_dimensions[0] * 0.75

        id = int(round(tank_length_partial * self.fuselage.step))

        height_fus_end = fuselage_heights[id]


        if outer_dimensions[0] <= height_fus_end and tank_length_full <= self.fuselage.Lmax:
            print("\nThe outer tank fits at the endpoint.")
        else:
            print(f"\nThe outer tank does not fit at the endpoint. \nTank height at endpoint: {height_fus_end}")

    def plot_tank_geometry(self):

        # TODO: Start with the outer tank

        # TODO: Calculate the ellipsoid coordinates at the elliptical domes


        # TODO: Append the constant radius for the cyllindrical part

        # TODO: Repeat for the inner tank

        plt.plot(self.fuselage.fuselage_lengths, self.fuselage.fuselage_height)
        plt.plot(self.fuselage.fuselage_lengths, -self.fuselage.fuselage_height)
        plt.show()



