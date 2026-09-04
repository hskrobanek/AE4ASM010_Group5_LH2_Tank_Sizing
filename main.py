from objects.fuselage import Fuselage, InnerTank, OuterTank, FitCheck
from cryotank_sizing.tank_general_properties import get_tank_volume, tank_height
from cryotank_sizing.outer_shell import *

# Define fuselage compartment geometry
Rmax = 0.450                  # [m]
Rmin = 0.300                  # [m]
Lmax = 1.150                  # [m]





offset = 0.010                # TODO: Determine the offset

# Define inner volume and precision
inner_volume = 0.298           # TODO: Determine the inner volume
step = 1000000

# Inputs
boil_off_rate = 0.1  # %/h, placeholder
density_LH2 = 70.85  # kg/m3
latent_heat = 447000  # J/kg
T_ext_env = 300 # K
thermalconductinner = 170

Qinneeded = heat_in_calculation(boil_off_rate, inner_volume, density_LH2, latent_heat)

height_array, length_array = tank_height(Rmax, Rmin, Lmax, step)
r_out = []
r_in = []

for i in range(len(height_array)):
    outer_radius = height_array[i]/2
    length = length_array[i]
    r_inner, r_outer = radius_outer(inner_volume, outer_radius, length, Qinneeded, thermalconductinner, 0.02, 300, 20)
    r_out.append(r_outer)
    r_in.append(r_inner)

# minimise length so first one in array
router = np.nonzero(r_in)[0]
rinner = np.nonzero(r_out)[0]
gap = router - rinner
fuselage = Fuselage(Rmax, Rmin, Lmax, step)
innertank = InnerTank(fuselage=fuselage, inner_volume=inner_volume, offset=offset, step=step)
outertank = OuterTank(fuselage = fuselage, inner_tank = innertank)
fit = FitCheck(fuselage = fuselage, innertank = innertank, outertank = outertank)

inner_dimensions = innertank.get_inner_tank_dimensions()
outer_dimensions = outertank.get_outer_tank_dimensions()

print(f'Inner tank dimensions: \nRadius: {round(inner_dimensions[0]*1000,5)} mm \nHeight: {inner_dimensions[0]*1000*0.75} mm \
        \nTotal length: {round(1000*(inner_dimensions[0]*0.75*2+inner_dimensions[1]),3)} mm  \nLength (cyllindrical part): {round(inner_dimensions[1]*1000,5)} mm \nVolume: {inner_dimensions[2]} m^3')
print('\n')
print(f'Outer tank dimensions: \nRadius: {round(outer_dimensions[0]*1000,5)} mm \nHeight: {round(outer_dimensions[0]*1000*0.75,5)} mm \
    \nTotal length: {round(1000*(outer_dimensions[0]*0.75*2+outer_dimensions[1]),5)} mm \nLength (cyllindrical part): {round(outer_dimensions[1]*1000,5)} mm \nVolume: {outer_dimensions[2]} m^3')

# Check if the tank fits inside the fuselage, i. e. if the outer shell radius is not greater than the fuselage height at the minimum fuselage height location

fit.check_if_outer_tank_fits()
