#!/usr/bin/env python

import RPi.GPIO as gpio

class Relay: 
  pin = 0 
  isOn = False
  invert = True
  
  def __init__(self, pin, invert=True): 
    self.pin = pin
    self.invert = invert
    gpio.setmode(gpio.BCM)
    gpio.setup(self.pin, gpio.OUT)
    if invert: 
      gpio.output(self.pin, not self.isOn)
    else: 
      gpio.output(self.pin, self.isOn)
      
      
  
  def on(self): 
    self.isOn = True
    if self.invert: 
      gpio.output(self.pin, False)
    else: 
      gpio.output(self.pin, True)
      
  def off(self): 
    self.isOn = False
    if self.invert: 
      gpio.output(self.pin, True)
    else: 
      gpio.output(self.pin, False)
