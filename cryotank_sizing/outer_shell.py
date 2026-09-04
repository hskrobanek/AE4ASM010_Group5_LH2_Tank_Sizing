# Inputs
boil_off_rate = 0.1  # %/h, placeholder
volume_LH2 = 10  # m3, placeholder
density_LH2 = 70.85  # kg/m3
latent_heat = 447000  # J/kg

def heat_in_calculation(boil_off_rate, volume_LH2, density_LH2, latent_heat):
    # BOR = (Qin * 24 * 3600 * 10) / (VLH2 * rhoLH2 * Hvap * 100)
    # rewrite to find Qin which then can be used to find the radii

    Qin = boil_off_rate / ((24*3600*10)/(volume_LH2*density_LH2*latent_heat*100))
    return Qin


def radius_outer(radius_inner, max_radius, thermal_conductivity_inner, ):
    # assume 1 metal liner of 1 mm as inner shell
    # assume 1 layer of air unknown thickness
    # assume 1 layer of metal 1 mm as outer shell
    radius_inner_plus_thickness = radius_inner + 1
    radius_left = max_radius
    # for loop that goes from inner radius to maximum to see if Qin is low enough 


    return outer_radius
