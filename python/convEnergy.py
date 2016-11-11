#!/usr/bin/env python

import sys, json, numpy as np
import astropy.units as u
import astropy.constants as const

# Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    lines = read_in()
    if (len(lines)==3):
        value1, unit1, unit2 = lines
    else:
        value1, unit1 = lines

    # display correlation between
    # 1 - energy
    # 2 - frequency (=E/h)
    # 3 - wavelength (=E/hc)
    # 4 - eV
    # 5 - T (=E/k)
    # 6 - E/m_e*c2
    # 7 - E/m_p*c2

    unit = u.Unit(unit1)
    # c0 = str(unit.to(u.erg, equivalencies=u.spectral()))+" erg"
    # c1 = str(unit.to(u.Hz, equivalencies=u.spectral()))+" Hz"
    # c2 = str(unit.to(u.AA, equivalencies=u.spectral()))+" AA"
    # c3 = str(unit.to(u.eV, equivalencies=u.spectral()))+" eV"
    # c4 = str(unit.to(u.K, equivalencies=u.temperature_energy()).value)+" K"
    # # unitless because the returned value is E/(m_e * c^2)
    # c5 = str(1.0 / const.m_e.to(unit, equivalencies=u.mass_energy()).value)
    # # unitless because the returned value is E/(m_p * c^2)
    # c6 = str(1.0 / const.m_p.to(unit, equivalencies=u.mass_energy()).value)

    # each print will be concatenated to the string
    # passed to the NodeJS server
    print(str((value1 * u.Unit(unit1)).to(u.Unit(unit2)))+", ")
    # print(c0+", ",c1+", ",c2+", ",c3+", ",c4+", ",c5+", ",c6)

#start process
if __name__ == '__main__':
    main()
