#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Week 6 Assignment - conversions"""

def convertcelciustokelvin(celciusmeasurement):
    celtokel = celciusmeasurement + 273.15
    celtokel = (round(celtokel,4))
    return celtokel

def convertcelciustofahrenheit(celciusmeasurement):
    celtofah = ((celciusmeasurement * 9.0) / 5.0) + 32.0
    celtofah = (round(celtofah,4))
    return celtofah

def convertfahrenheittocelsius(fahrenheitmeasurement):
    fahtocel = ((fahrenheitmeasurement - 32.0) * 5.0) / 9.0
    fahtocel = (round(fahtocel,4))
    return fahtocel

def convertfahrenheittokelvin(fahrenheitmeasurement):
    fahtokel = ((fahrenheitmeasurement + 459.67) * 5.0) / 9.0
    fahtokel = (round(fahtokel,4))
    return fahtokel

def convertkelvintofahrenheit(kelvinmeasurement):
    keltofah = ((kelvinmeasurement * 9.0) / 5.0) - 459.67
    keltofah = (round(keltofah,4))
    return keltofah

def cconvertkelvintocelcius(kelvinmeasurement):
    keltocel = kelvinmeasurement - 273.15
    keltocel = (round(keltocel,4))
    return keltocel
