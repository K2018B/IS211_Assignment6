#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Week 6 Assignment - tests"""

import conversions, unittest

class ConvertCelToKelTest(unittest.TestCase):
    knownvalues = ((6, 279.15), (10, 283.15), (35, 308.15), (89, 362.15), (102, 375.15))

    def testceltokel(self):
        """to Kelvin should give known result with know input"""
        for cel, kel in self.knownvalues:
            result = conversions.convertcelciustokelvin(cel)
            self.assertEqual(kel, result)

class ConvertCelToFahTest(unittest.TestCase):
    knownvalues = ((6, 42.8), (10, 50), (35, 95), (89, 192.2), (102, 215.6))

    def testceltofah(self):
        """to Fahrenheit should give known result with know input"""
        for cel, fah in self.knownvalues:
            result = conversions.convertcelciustofahrenheit(cel)
            self.assertEqual(fah, result)
            
class ConvertFahToCelTest(unittest.TestCase):
    knownvalues = ((90, 32.2222), (95, 35), (120, 48.8889), (130, 54.4444), (132, 55.5556))

    def testfahtocel(self):
        """to Fahrenheit should give known result with know input"""
        for fah, cel in self.knownvalues:
            result = conversions.convertfahrenheittocelsius(fah)
            self.assertEqual(cel, result)

class ConvertFahTokelTest(unittest.TestCase):
    knownvalues = ((80, 299.8167), (100, 310.9278), (150, 338.7056), (175, 352.5944), (180, 355.3722))

    def testfahtokel(self):
        """to Fahrenheit should give known result with know input"""
        for fah, kel in self.knownvalues:
            result = conversions.convertfahrenheittokelvin(fah)
            self.assertEqual(kel, result)            
            
class ConvertKelToFahTest(unittest.TestCase):
    knownvalues = ((500, 440.33), (350, 170.33), (300, 80.33), (280, 44.33), (275, 35.33))

    def testkeltofah(self):
        """to Fahrenheit should give known result with know input"""
        for kel, fah in self.knownvalues:
            result = conversions.convertkelvintofahrenheit(kel)
            self.assertEqual(fah, result)

class ConvertKelToCelTest(unittest.TestCase):
    knownvalues = ((500, 226.85), (450, 176.85), (435, 161.85), (420, 146.85), (350, 76.85))

    def testkeltocel(self):
        """to Fahrenheit should give known result with know input"""
        for kel, cel in self.knownvalues:
            result = conversions.cconvertkelvintocelcius(kel)
            self.assertEqual(cel, result)

if __name__ == '__main__':
    unittest.main()
