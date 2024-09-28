# api.py

import os
import logging
from webob import Request, Response

logging.basicConfig(level=logging.DEBUG)

class API:
    def __init__(self):
        self.routes = {}
        self.static_dir = "static"

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)
    
    def handle_request(self, request):
        response = Response()

        if request.path.startswith("/static"):
            # logging.debug(f"Static file request: {request.path}")
            self.serve_static(request, response)
            return response

        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, response)
                return response

        self.default_response(response)
        return response

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."
    
    def serve_static(self, request, response):
        file_path = request.path[len("/static/"):]
        full_path = os.path.join(self.static_dir, file_path)
        # logging.debug(f"Serving static file: {full_path}")

        if os.path.isfile(full_path):
            response.status_code = 200
            response.content_type = self.get_file_type(full_path)
            with open(full_path, "rb") as file:
                response.body = file.read()
        else:
            logging.debug(f"File not found: {full_path}")
            self.default_response(response)
    
    def get_file_type(self, file_path):
        file_ext = os.path.splitext(file_path)[1]
        return {
            ".html": "text/html",
            ".css": "text/css",
            ".js": "text/javascript",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".svg": "image/svg+xml",
        }.get(file_ext, 'application/octet-stream')