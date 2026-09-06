import numpy as np
import matplotlib.pyplot as plt
from objects.fuselage import Fuselage
from objects.inner_tank import InnerTank
from objects.outer_tank import OuterTank

class GeometryPlot:
    def __init__(self,fuselage, inner_tank, outer_tank):
        self.fuselage = fuselage
        self.innertank = inner_tank
        self.outertank = outer_tank

    def get_tank_shape(self, inner_tank:bool, outer_tank:bool):


        if inner_tank:
            offset = self.innertank.offset
            a = self.innertank.get_inner_tank_dimensions()[0]
            b = a * 0.75
            length = self.innertank.get_inner_tank_dimensions()[1]

        if outer_tank:
            offset = 0.0
            a = self.outertank.get_outer_tank_dimensions()[0]
            b = a * 0.75
            length = self.outertank.get_outer_tank_dimensions()[1]

    # Left dome:
        theta1 = np.linspace(np.pi/2, 3*np.pi/2, self.fuselage.step)
        x1 = b * np.cos(theta1) + offset + b
        y1 = a * np.sin(theta1)
        plt.plot(x1,y1, 'r' if inner_tank else 'b')

    # Main body:
        xb = np.linspace(offset+b,offset + b +length,self.fuselage.step)
        yb = np.ones(self.fuselage.step) * a
        plt.plot(xb,yb, 'r' if inner_tank else 'b')
        plt.plot(xb,-yb, 'r' if inner_tank else 'b')


    # Right dome:
        theta2 = np.linspace(np.pi*3/2, np.pi*5/2, self.fuselage.step)
        x2 = b * np.cos(theta2) + length + b + offset
        y2 = a * np.sin(theta2)
        plt.plot(x2,y2, 'r' if inner_tank else 'b')

    # Fuselage:
        if inner_tank:
            x_fuselage = self.fuselage.fuselage_lengths
            y_fuselage = self.fuselage.fuselage_height
            plt.plot(x_fuselage, y_fuselage, 'black')
            plt.plot(x_fuselage, -y_fuselage, 'black')






