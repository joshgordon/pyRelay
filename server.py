#!/usr/bin/env python 

import relay
import bottle
import json 
import threading
import http_server
import xmlrpc_server
from box import Box

box = Box() 


t = threading.Thread(target=http_server.startServer, args=(box, ))
t.daemon = True
t.start() 

t1 = threading.Thread(target=xmlrpc_server.startServer, args=(box, ))
t1.daemon = True
t1.start() 


# ugly hack, but works. 
t.join()
