import http.server # libraries to create web server, create http server
import socketserver

#create variable to handle requests from client
handler = http.server.SimpleHTTPRequestHandler

#start transmision use port 1234
with socketserver.TCPServer(("", 1234), handler) as http:
    http.serve_forever() # to keep server running, waiting
                         # requests from client                        

