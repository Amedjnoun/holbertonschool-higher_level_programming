#!/usr/bin/python3

"""
This module fetches posts from JSONPlaceholder API and performs two operations:
1. Prints post titles to console
2. Saves posts data to a CSV file
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(b'version": "1.0", '
                          b'"description": "A simple API built with '
                          b'http.server')
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


def run(
        server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler,
        port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
