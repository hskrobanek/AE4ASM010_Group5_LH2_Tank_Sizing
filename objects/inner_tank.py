import numpy as np
from cryotank_sizing.tank_general_properties import tank_height, get_tank_volume


class InnerTank:
    def __init__ (self, fuselage, inner_volume, offset):
        self.inner_volume = inner_volume
        self.fuselage = fuselage
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
        rmax = self.fuselage.Rmax - self.offset
        rmin = self.fuselage.Rmin - self.offset
        lmax = self.fuselage.Lmax - 2*rmin*0.75 - 2*self.offset


        #Compute the maximum internal tank height at each length increment
        lengths = self.fuselage.fuselage_lengths
        height_inner, _ = tank_height(rmax,rmin,self.fuselage.Lmax,len(lengths))

        # Set up the loop
        solution = False
        i=0


        # Iterate until the first radius-length combination is found for which the inner volume requirement is satisfied
        # The design is optimised for the highest surface area-to-volume ratio, i. e. the highest R/L
        while i < len(lengths):

            # TODO: Take the inner radius and calculate the location of the tangency point
            radius_inner = height_inner[i]
            H_inner = 0.75*radius_inner

            id = int((H_inner+lengths[i])*self.fuselage.step)

            # TODO: Based on the tangecy point, find the corresponding inner tank height
            radius_inner_tan = height_inner[id]

            # TODO: Calculate the volume of the tank with the newly found radius


            volume = get_tank_volume(radius_inner_tan, lengths[i])

            if volume >= self.inner_volume:
                inner_dimensions = (radius_inner_tan, lengths[i], volume)
            #if np.abs(volume - self.inner_volume) < 1e-6:
            #    inner_dimensions = ([round(float(height_updated),5), round(float(lengths[i]),5), round(float(volume),5)])
                solution = True
                break
            i+=1
        # Evaluate whether a solution has been found
        if not solution:
            raise ValueError("No inner tank solution found for the given volume")

        return inner_dimensions
