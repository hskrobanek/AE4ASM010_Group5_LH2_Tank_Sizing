from objects.fuselage import Fuselage, InnerTank, OuterTank
from cryotank_sizing.tank_general_properties import get_tank_volume, tank_height

# Define fuselage compartment geometry
Rmax = 0.425
Rmin = 0.285
Lmax = 1.135
offset = 0.010

# Define inner volume and precision
inner_volume = 0.23
step = 1000

fuselage = Fuselage(Rmax, Rmin, Lmax)
innertank = InnerTank(fuselage=fuselage, inner_volume=inner_volume, offset=offset, step=step)
outertank = OuterTank(fuselage = fuselage, inner_tank = innertank)

inner_dimensions = innertank.get_inner_tank_dimensions()
outer_dimensions = outertank.get_outer_tank_dimensions()

print(f'Inner tank dimensions: \nRadius: {inner_dimensions[0]*1000} mm \nHeight: {inner_dimensions[0]*1000*0.75} mm \
        \nTotal length: {1000*(inner_dimensions[0]*0.75*2+inner_dimensions[1])} mm  \nLength (cyllindrical part): {inner_dimensions[1]*1000} mm \nVolume: {inner_dimensions[2]} m^3')
print('\n')
print(f'Outer tank dimensions: \nRadius: {outer_dimensions[0]*1000} mm nHeight: {inner_dimensions[0]*1000*0.75} mm \
    \nTotal length: {1000*(inner_dimensions[0]*0.75*2+inner_dimensions[1])} mm \nLength (cyllindrical part): {outer_dimensions[1]*1000} mm \nVolume: {outer_dimensions[2]} m^3')
