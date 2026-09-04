import numpy as np
from cryotank_sizing.tank_general_properties import get_tank_volume
# Inputs
boil_off_rate = 0.1  # %/h, placeholder
volume_LH2 = 0.3  # m3, placeholder
density_LH2 = 70.85  # kg/m3
latent_heat = 447000  # J/kg
T_ext_env = 300 # K

def heat_in_calculation(boil_off_rate, volume_LH2, density_LH2, latent_heat):
    # BOR = (Qin * 24 * 3600 * 10) / (VLH2 * rhoLH2 * Hvap * 100)
    # rewrite to find Qin which then can be used to find the radii

    Qin = boil_off_rate / ((24*3600*10)/(volume_LH2*density_LH2*latent_heat*100))
    return Qin


def radius_outer(volumeLH2, max_radius, Length, Qin_needed, thermal_conductivity_inner, thermal_conductivity_air, T_ext_env, T_int_surface,previous_volume = 100, h = 25, final_inner_radius = 0, final_outer_radius = 0):
    # assume 1 metal liner of 1 mm as inner shell
    # assume 1 layer of air unknown thickness
    # assume 1 layer of metal 1 mm as outer shell
    r_external = max_radius
    # for loop that goes from inner radius to maximum to see if Qin is low enough 
    for i in range(int(max_radius)):
        r_inner = max_radius - i
        radius_inner_plus_thickness = r_inner + 1
        r_inner_ratio = r_inner / radius_inner_plus_thickness
        tank_volume = get_tank_volume(r_inner, Length)
        for j in range(r_external-r_inner):
            r_vaccuum_ratio = (r_inner + j)/(r_external - 1) 
            Qin = (T_ext_env - T_int_surface)/(np.log(r_inner_ratio)/(2 * np.pi * thermal_conductivity_inner * Length) + np.log(r_vaccuum_ratio)/(2 * np.pi *thermal_conductivity_air * Length) + 1 / (2 * np.pi * r_external * Length * h))

            if Qin<=Qin_needed and tank_volume>=volumeLH2 and tank_volume<=previous_volume:
                previous_volume = tank_volume
                final_inner_radius = r_inner
                final_outer_radius = r_external



    return final_inner_radius, final_outer_radius
