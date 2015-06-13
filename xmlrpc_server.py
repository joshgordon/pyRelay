from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import box



def startServer(box): 

    # Restrict to a particular path.
    class RequestHandler(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2',)

    # Create server
    server = SimpleXMLRPCServer(("0.0.0.0", 8000),
                                requestHandler=RequestHandler, allow_none=True)
    server.register_introspection_functions()
    
    server.register_instance(box)
    
    # Run the server's main loop
    server.serve_forever()
