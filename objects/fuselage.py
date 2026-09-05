import numpy as np

from cryotank_sizing.tank_general_properties import tank_height, get_tank_volume

class Fuselage:
    def __init__(self, Rmax, Rmin, Lmax, step):
        self.Rmax = Rmax
        self.Rmin = Rmin
        self.Lmax = Lmax
        self.step = step
        self.fuselage_lengths = np.arange(0,self.Lmax,1/self.step)
        self.fuselage_height, _ = tank_height(self.Rmax,self.Rmin,self.Lmax,len(self.fuselage_lengths))





