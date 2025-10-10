#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socketserver


class SimpleServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Traite les endpoints /, /data et /info
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/info":
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("404 Not Found".encode())


PORT = 8000
server = socketserver.TCPServer(("", PORT), SimpleServer)
server.serve_forever()
