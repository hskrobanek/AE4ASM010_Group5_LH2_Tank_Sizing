import numpy as np
from cryotank_sizing.tank_general_properties import tank_height, get_tank_volume

class Fuselage:
    def __init__(self, Rmax, Rmin, Lmax, step):
        self.Rmax = Rmax
        self.Rmin = Rmin
        self.Lmax = Lmax
        self.step = step

    def get_height_profile(self):
        lengths = np.arange(0,self.Lmax,1/self.step)
        height = tank_height(self.Rmax,self.Rmin,self.Lmax,len(lengths))
        return height


class InnerTank:
    def __init__ (self, fuselage, inner_volume, offset, step):
        self.inner_volume = inner_volume
        self.fuselage = fuselage
        self.Rmax = fuselage.Rmax
        self.Rmin = fuselage.Rmin
        self.Lmax = fuselage.Lmax
        self.offset = offset

    def get_inner_tank_dimensions(self):
        '''
        inputs:
            inner_volume --> the required inner tank volume for LH2
            Rmax --> the maximum outer tank radius based on AC geometry
            Rmin --> the minimum outer tank radius based on AC geometry
            Lmax --> the maximum length of the tank (cyllindrical + elliptical parts) based on AC geometry
        '''

        #Calculate max internal tank properties from available space within the fuselage
        rmax = self.Rmax - self.offset
        rmin = self.Rmin - self.offset
        lmax = self.Lmax - 2*rmin*0.75 - 2*self.offset


        #Compute the tank height at each length increment starting from Rmax
        lengths = np.arange(0,lmax,1/self.fuselage.step)
        height_inner = tank_height(rmax,rmin,lmax,len(lengths))
        height_fuselage = self.fuselage.get_height_profile()
        height_total = tank_height(self.Rmax, self.Rmin, self.Lmax, len(lengths))

        # Set up the while loop
        solution = False
        i = 0

        # Iterate until the first radius-length combination is found for which the inner volume requirement is satisfied
        # The design is optimised for the highest surface area-to-volume ratio, i. e. the highest R/L

        while i < len(lengths):
            volume = get_tank_volume(height_inner[i], lengths[i])
            if volume >= self.inner_volume:
                inner_dimensions = ([round(float(height_inner[i]),5), round(float(lengths[i]),5), round(float(volume),5)])
                solution = True
                break
            i+=1

        # Evaluate whether a solution has been found
        if not solution:
            raise ValueError("No inner tank solution found for the given volume")


        return inner_dimensions


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
        fuselage_heights = self.fuselage.get_height_profile()

        tank_length = outer_dimensions[0] * 0.75 + outer_dimensions[1]
        id = int(round(tank_length * self.fuselage.step))

        height_fus_end = fuselage_heights[id]


        if outer_dimensions[0] >= height_fus_end:
            print("The outer tank fits at the endpoint.")
        else:
            print("The outer tank does not fit at the endpoint.")



