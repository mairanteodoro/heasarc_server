#!/usr/bin/env python

import sys, json, numpy as np
from astropy.time import Time
import astropy.constants as const

# Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    lines = read_in()

    t = Time(lines, format='isot', scale='utc')

    result = {"date": t.value,
              "JD": t.jd,
              "MJD": t.mjd,
              "decimalYr": t.decimalyear,
    }

    # each print will be concatenated to the string
    # passed to the NodeJS server
    print(str(result))

#start process
if __name__ == '__main__':
    main()
