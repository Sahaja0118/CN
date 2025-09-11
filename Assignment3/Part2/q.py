import socket

HOST = "127.0.0.1"
PORT = 8080

def parse_headers(request):
    """Extract headers from raw HTTP request."""
    headers = {}
    lines = request.split("\r\n")
    for line in lines[1:]:  
        if ": " in line:
            key, value = line.split(": ", 1)
            headers[key] = value
    return headers

def build_response(body, set_cookie=None):
    """Build HTTP response with optional Set-Cookie header."""
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n"
    if set_cookie:
        response += f"Set-Cookie: {set_cookie}\r\n"
    response += f"Content-Length: {len(body)}\r\n"
    response += "Connection: close\r\n\r\n"
    response += body
    return response

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Server running on http://{HOST}:{PORT}/")

        while True:
            conn, addr = s.accept()
            with conn:
                request = conn.recv(1024).decode("utf-8")
                if not request:
                    continue

                headers = parse_headers(request)

                cookie = headers.get("Cookie")

                if cookie:
                    body = f"<h1>Welcome back! Your cookie: {cookie}</h1>"
                    response = build_response(body)
                else:
                    body = "<h1>Hello, new user! Setting your cookie...</h1>"
                    response = build_response(body, set_cookie="UserID=User123")

                conn.sendall(response.encode("utf-8"))

if __name__ == "__main__":
    run_server()
