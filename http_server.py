#!/usr/bin/env python 

import relay
import bottle
import json 
from box import Box

  
def startServer(box):
  @bottle.route("/<num>/on")
  def on(num): 
    box.on(int(num))

  @bottle.route("/<num>/off")
  def off(num): 
    box.off(int(num))

  @bottle.route("/<num>/state")
  def singleState(num): 
    return box.state(int(num))
    
  @bottle.route("/state")
  def state(): 
    bottle.response.content_type = 'application/json'
    return json.dumps(box.allState())

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
