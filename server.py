import time
import BaseHTTPServer
import json, os
from urlparse import urlparse, parse_qs

from predictive_text import get_suggestions

HOST_NAME = "0.0.0.0"
PORT_NUMBER = 8080

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    def do_GET(self):
        """Respond to a GET request."""
        
        query_components = parse_qs(urlparse(self.path).query)
        word = query_components["word"][0]
        
        print time.asctime(), "Request suggestions for - %s" % (word)
        
        suggestions = get_suggestions(word)
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(suggestions))
        
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)