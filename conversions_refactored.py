#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Week 6 Assignment - conversions_refactored"""

from __future__ import division

class ConversionNotPossible(Exception): pass

conversionsunits = {
    ("miles", "yards"):("measurement * 1760.00"),
    ("miles", "meter"):("measurement * 1609.34"),
    ("yards", "miles"):("measurement / 1760"),
    ("yards", "meter"):("measurement * 0.9144"),
    ("meter", "miles"):("measurement / 1609.34"),
    ("meter", "yards"):("measurement * 1.09361"),   
    ("celsius", "kelvin"):("measurement + 273.15"),
    ("celsius", "fahrenheit"):("(((measurement * 9.0) / 5.0) + 32.0)"),
    ("fahrenheit", "celsius"):("(((measurement - 32.0) * 5.0) / 9.0)"),
    ("fahrenheit", "kelvin"): ("(((measurement + 459.67) * 5.0) / 9.0)"),
    ("kelvin", "fahrenheit"):("(((measurement * 9.0) / 5.0) - 459.67)"),
    ("kelvin", "celsius"):("measurement - 273.15")
    }

def convert(fromunit, tounit, value):
    if (fromunit,tounit) in conversionsunits.keys():
        measurement = value
        conversion = eval(conversionsunits[(fromunit, tounit)])
        conversion = (round(conversion,4))
        return conversion        
    else:
        raise ConversionNotPossible, "incompatible units"
