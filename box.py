#!/usr/bin/env pytyhon 

import relay

class Box: 
  pinAssignment = list([14, 15, 18, 23, 24, 25, 9, 11])
  relays = list() 

  
  def __init__(self): 
    for pin in self.pinAssignment: 
      self.relays.append(relay.Relay(pin))

  def on(self, relay): 
    self.relays[relay - 1].on()

  def off(self, relay): 
    self.relays[relay - 1].off() 

  def state(self, relay): 
    return self.relays[relay - 1].isOn

  def allState(self): 
    return list(map(lambda r: r.isOn, self.relays))
