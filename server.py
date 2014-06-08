#!/usr/bin/env python 

import relay
import bottle
import json 

pinAssignment = list([14, 15, 18, 23, 24, 25, 9, 11])
relays = list() 

for pin in pinAssignment: 
  relays.append(relay.Relay(pin))
  
  
@bottle.route("/<num>/on")
def on(num): 
  relays[int(num) - 1].on() 

@bottle.route("/<num>/off")
def off(num): 
  relays[int(num) - 1].off()

@bottle.route("/<num>/state")
def singleState(num): 
  return relays[int(num) -1].isOn

@bottle.route("/state")
def state(): 
  bottle.response.content_type = 'application/json'
  return json.dumps(list(map(lambda r: r.isOn, relays)))

@bottle.route("/")
def root(): 
  return bottle.static_file("index.html", root="/home/josh/pyRelay")

@bottle.route("/magic.js")
def js(): 
  return bottle.static_file("magic.js", root="/home/josh/pyRelay")

@bottle.route("/switch-off.jpg")
def switchOff(): 
  return bottle.static_file("switch-off.jpg", root="/home/josh/pyRelay")

@bottle.route("/switch-on.jpg")
def switchOn(): 
  return bottle.static_file("switch-on.jpg", root="/home/josh/pyRelay")

bottle.run(host='0.0.0.0')
