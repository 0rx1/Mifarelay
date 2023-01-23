import signal
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        json_data = json.loads(body)
        uid = json_data["uid"]
        print(f"Received UID: {uid}")
        with open("UIDs.txt", "a") as f:
            f.write(f"{uid}\n")
        self._send_response("UID received")

def run():
    server_address = ("", 8008)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Listening on localhost:8080")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server...")
        httpd.server_close()

run()
