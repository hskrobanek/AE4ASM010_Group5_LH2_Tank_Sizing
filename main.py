import math


# Material: given metal
yield_strength = 345e6    # Pa
safety_factor = 1.0       

# Geometry
R = 0.2
H = 0.1

p = 10e5   


# 0 deg  = top of the dome
# 90 deg = dome/cylinder transition
angles_deg = [0, 30, 60, 90]


# CALCULATIONS

allowable_stress = yield_strength / safety_factor
gamma = R**2 / H**2 - 1


def von_mises(s1, s2):
    # Equivalent stress for a 2D (thin-walled) stress state
    return math.sqrt(s1**2 - s1 * s2 + s2**2)


# all stresses scale with 1/t. So we calculate them for t = 1 m,
# then the needed thickness is: t_min = stress(t=1) / allowable_stress
t = 1

print("gamma =", gamma)
print("Allowable stress =", allowable_stress / 1e6, "MPa")
print("Pressure =", p / 1e5, "bar")
print()

# ---------- Ellipsoidal dome ----------
print("DOME")
print(f"{'angle':>6} {'sigma_m*t':>12} {'sigma_h*t':>12} {'sigma_vm*t':>12} {'t_min':>10}")
print(f"{'[deg]':>6} {'[N/m]':>12} {'[N/m]':>12} {'[N/m]':>12} {'[mm]':>10}")

t_dome = 0
for angle in angles_deg:
    theta = math.radians(angle)
    sin2 = math.sin(theta) ** 2

    sigma_m = (p * R / (2 * t)) * math.sqrt((1 + gamma) / (1 + gamma * sin2))
    sigma_h = (1 - gamma * sin2) * sigma_m
    sigma_vm = von_mises(sigma_m, sigma_h)

    t_needed = sigma_vm / allowable_stress
    t_dome = max(t_dome, t_needed)

    print(f"{angle:>6} {sigma_m:>12.1f} {sigma_h:>12.1f} {sigma_vm:>12.1f} {t_needed*1000:>10.4f}")

# ---------- Cylinder ----------
sigma_hoop_cyl = p * R / t
sigma_axial_cyl = p * R / (2 * t)
sigma_vm_cyl = von_mises(sigma_hoop_cyl, sigma_axial_cyl)
t_cyl = sigma_vm_cyl / allowable_stress

print()
print("CYLINDER")
print(f"sigma_hoop*t  = {sigma_hoop_cyl:.1f} N/m")
print(f"sigma_axial*t = {sigma_axial_cyl:.1f} N/m")
print(f"sigma_vm*t    = {sigma_vm_cyl:.1f} N/m")

print()
print(f"Minimum dome thickness     = {t_dome*1000:.4f} mm")
print(f"Minimum cylinder thickness = {t_cyl*1000:.4f} mm")