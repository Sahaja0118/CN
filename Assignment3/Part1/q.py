import http.server
import socketserver
import os
import hashlib
import time
import email.utils

PORT = 8080
FILE = "index.html"

class CachingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            if not os.path.exists(FILE):
                self.send_error(404, "File not found")
                return

            with open(FILE, "rb") as f:
                content = f.read()

            etag = hashlib.md5(content).hexdigest()

            last_modified_time = os.path.getmtime(FILE)
            last_modified_http = email.utils.formatdate(
                timeval=last_modified_time, usegmt=True
            )

            if_none_match = self.headers.get("If-None-Match")
            if_modified_since = self.headers.get("If-Modified-Since")

            if if_none_match == etag:
                self.send_response(304)
                self.end_headers()
                return

            if if_modified_since:
                req_time = email.utils.parsedate_to_datetime(if_modified_since)
                file_time = email.utils.parsedate_to_datetime(last_modified_http)
                if file_time <= req_time:
                    self.send_response(304)
                    self.end_headers()
                    return

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("ETag", etag)
            self.send_header("Last-Modified", last_modified_http)
            self.end_headers()
            self.wfile.write(content)

        else:
            super().do_GET()


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CachingHTTPRequestHandler) as httpd:
        print(f"Serving on port {PORT}...")
        # Open browser -> http://localhost:8080
        httpd.serve_forever()
