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
    value1, unit1, unit2 = lines

    # display correlation between
    # 1 - energy
    # 2 - frequency
    # 3 - wavelength
    # 4 - eV
    # 5 - T
    # 6 - m_e
    # 7 - m_p

    unit = u.Unit(unit1)
    c1 = unit.to(u.Hz, equivalencies=u.spectral())
    c2 = unit.to(u.AA, equivalencies=u.spectral())
    c3 = unit.to(u.eV, equivalencies=u.spectral())
    c4 = unit.to(u.K, equivalencies=u.temperature_energy()).value
    c5 = 1.0 / const.m_e.to(unit, equivalencies=u.mass_energy()).value
    c6 = 1.0 / const.m_p.to(unit, equivalencies=u.mass_energy()).value

    print((value1 * u.Unit(unit1)).to(u.Unit(unit2)))
    print([c1,c2,c3,c4,c5,c6])

#start process
if __name__ == '__main__':
    main()
