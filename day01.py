#!/usr/bin/env python

from math import floor

f = open('day01_input.txt', 'r')
masses = f.readlines()
f.close()

sum_fuel = 0
for m in masses:
    mass = int(m)
    sum_fuel += floor(mass/3)-2
print(sum_fuel)

recursive_sum_fuel = 0
for m in masses:
    mass = int(m)
    fuel_mass = floor(mass/3)-2
    recursive_sum_fuel += fuel_mass
    while fuel_mass >= 9:
        fuel_mass = floor(fuel_mass/3)-2
        recursive_sum_fuel += fuel_mass
print(recursive_sum_fuel)
