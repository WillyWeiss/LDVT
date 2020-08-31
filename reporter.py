#Make all imports
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

# Declare variable
HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

#Setup server paramaeters
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
    
#Server IP address
server_address = ('127.0.0.1', port)

#Home Page
path = 'index.html'

## Handle the connection
HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)
sa = httpd.socket.getsockname()
## Let the use know that server is up and running.
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
