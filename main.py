from objects.fuselage import Fuselage, InnerTank, OuterTank
from cryotank_sizing.tank_general_properties import get_tank_volume, tank_height

# Define fuselage compartment geometry
Rmax = 0.450                  # [m]
Rmin = 0.300                  # [m]
Lmax = 1.150                  # [m]
offset = 0.010                # TODO: Determine the offset

# Define inner volume and precision
inner_volume = 0.298           # TODO: Determine the inner volume
step = 100000

fuselage = Fuselage(Rmax, Rmin, Lmax)
innertank = InnerTank(fuselage=fuselage, inner_volume=inner_volume, offset=offset, step=step)
outertank = OuterTank(fuselage = fuselage, inner_tank = innertank)

inner_dimensions = innertank.get_inner_tank_dimensions()
outer_dimensions = outertank.get_outer_tank_dimensions()

print(f'Inner tank dimensions: \nRadius: {round(inner_dimensions[0]*1000,5)} mm \nHeight: {inner_dimensions[0]*1000*0.75} mm \
        \nTotal length: {round(1000*(inner_dimensions[0]*0.75*2+inner_dimensions[1]),3)} mm  \nLength (cyllindrical part): {round(inner_dimensions[1]*1000,5)} mm \nVolume: {inner_dimensions[2]} m^3')
print('\n')
print(f'Outer tank dimensions: \nRadius: {round(outer_dimensions[0]*1000,5)} mm \nHeight: {round(inner_dimensions[0]*1000*0.75,5)} mm \
    \nTotal length: {round(1000*(inner_dimensions[0]*0.75*2+inner_dimensions[1]),5)} mm \nLength (cyllindrical part): {round(outer_dimensions[1]*1000,5)} mm \nVolume: {outer_dimensions[2]} m^3')
