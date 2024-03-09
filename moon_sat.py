# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:03:34 2024

@author: iamrs
"""

import math

# Constants
G = 6.674 * (10 ** -11)  # gravitational constant (m^3/kg/s^2)
earth_mass = 5.972 * (10 ** 24)  # mass of Earth (kg)
moon_mass = 7.347 * (10 ** 22)  # mass of Moon (kg)
earth_radius = 6.371 * (10 ** 6)  # radius of Earth (m)
moon_radius = 1.737 * (10 ** 6)  # radius of Moon (m)
moon_distance = 384 * (10 ** 6)  # average distance from Earth to Moon (m)

# Initial conditions
satellite_distance = earth_radius  # initial distance of satellite from Earth's center (m)
satellite_velocity = math.sqrt(G * earth_mass / satellite_distance)  # initial velocity of satellite (m/s)
time_step = 1  # time step for simulation (s)
total_time = 0  # total simulation time (s)

# Simulation loop
while satellite_distance < moon_distance:
    # Calculate gravitational force exerted by Earth and Moon
    force_earth = G * earth_mass * moon_mass / (satellite_distance ** 2)
    force_moon = G * moon_mass * earth_mass / ((moon_distance - satellite_distance) ** 2)

    # Calculate net force on satellite
    net_force = force_earth - force_moon

    # Calculate acceleration of satellite
    acceleration = net_force / earth_mass

    # Update velocity of satellite
    satellite_velocity += acceleration * time_step

    # Update distance of satellite from Earth's center
    satellite_distance += satellite_velocity * time_step

    # Update simulation time
    total_time += time_step

# Output
print("Satellite reached the Moon after", total_time, "seconds.")
