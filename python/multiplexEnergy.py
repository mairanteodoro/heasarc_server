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
    value1, unit1 = lines

    # display correlation between
    # 1 - energy
    # 2 - frequency (=E/h)
    # 3 - wavelength (=E/hc)
    # 4 - eV
    # 5 - T (=E/k)
    # 6 - E/m_e*c2
    # 7 - E/m_p*c2

    if (unit1=="mp") | (unit1=="m_p"):
        unit = value1 * const.m_p
    else:
        if (unit1=="me") | (unit1=="m_e"):
            unit = value1 * const.m_e
        else:
            unit = value1 * u.Unit(unit1)

    if (unit.unit.name=="K"):
        # convert everything from K to erg first
        c0 = str(unit.to(u.erg, equivalencies=u.temperature_energy()))
        temp = unit.to(u.erg, equivalencies=u.temperature_energy())
        c1 = str(temp.to(u.Hz, equivalencies=u.spectral()))
        temp = unit.to(u.erg, equivalencies=u.temperature_energy())
        c2 = str(temp.to(u.AA, equivalencies=u.spectral()))
        temp = unit.to(u.erg, equivalencies=u.temperature_energy())
        c3 = str(temp.to(u.eV, equivalencies=u.spectral()))
        c4 = str(unit.to(u.K, equivalencies=u.temperature_energy()).value)+" K"
        # unitless because the returned value is E/(m_e * c^2)
        temp = unit.to(u.erg, equivalencies=u.temperature_energy())
        c5 = str(1.0 / const.m_e.to(temp, equivalencies=u.mass_energy()).value)
        # unitless because the returned value is E/(m_p * c^2)
        temp = unit.to(u.erg, equivalencies=u.temperature_energy())
        c6 = str(1.0 / const.m_p.to(temp, equivalencies=u.mass_energy()).value)
    else:
        if (unit.unit.name=="erg") | (unit.unit.name=="eV"):
            c0 = str(unit.to(u.erg, equivalencies=u.spectral()))
            c1 = str(unit.to(u.Hz, equivalencies=u.spectral()))
            c2 = str(unit.to(u.AA, equivalencies=u.spectral()))
            c3 = str(unit.to(u.eV, equivalencies=u.spectral()))
            c4 = str(unit.to(u.K, equivalencies=u.temperature_energy()).value)+" K"
            # unitless because the returned value is E/(m_e * c^2)
            c5 = str(1.0 / const.m_e.to(unit, equivalencies=u.mass_energy()).value)
            # unitless because the returned value is E/(m_p * c^2)
            c6 = str(1.0 / const.m_p.to(unit, equivalencies=u.mass_energy()).value)
        else:
            if (unit.unit.name=="Hz") | (unit.unit.name=="Angstrom"):
                c0 = str(unit.to(u.erg, equivalencies=u.spectral()))
                c1 = str(unit.to(u.Hz, equivalencies=u.spectral()))
                c2 = str(unit.to(u.AA, equivalencies=u.spectral()))
                c3 = str(unit.to(u.eV, equivalencies=u.spectral()))
                temp = unit.to(u.erg, equivalencies=u.spectral())
                c4 = str(temp.to(u.K, equivalencies=u.temperature_energy()).value)+" K"
                # unitless because the returned value is E/(m_e * c^2)
                temp = unit.to(u.erg, equivalencies=u.spectral())
                c5 = str(1.0 / const.m_e.to(temp, equivalencies=u.mass_energy()).value)
                # unitless because the returned value is E/(m_p * c^2)
                temp = unit.to(u.erg, equivalencies=u.spectral())
                c6 = str(1.0 / const.m_p.to(temp, equivalencies=u.mass_energy()).value)
            else:
                c0 = str(unit.to(u.erg, equivalencies=u.mass_energy()))
                temp = unit.to(u.erg, equivalencies=u.mass_energy())
                c1 = str(temp.to(u.Hz, equivalencies=u.spectral()))
                c2 = str(temp.to(u.AA, equivalencies=u.spectral()))
                c3 = str(temp.to(u.eV, equivalencies=u.spectral()))
                temp = unit.to(u.erg, equivalencies=u.mass_energy())
                c4 = str(temp.to(u.K, equivalencies=u.temperature_energy()).value)+" K"
                # unitless because the returned value is E/(m_e * c^2)
                c5 = str(1.0 / const.m_e.to(unit, equivalencies=u.mass_energy()).value)
                # unitless because the returned value is E/(m_p * c^2)
                c6 = str(1.0 / const.m_p.to(unit, equivalencies=u.mass_energy()).value)
                # c0,c1,c2,c3,c4,c5,c6 = "1","1","1","1","1","1","1"

    # each print will be concatenated to the string
    # passed to the NodeJS server
    print(c0+",",c1+",",c2+",",c3+",",c4+",",c5+",",c6)

#start process
if __name__ == '__main__':
    main()
