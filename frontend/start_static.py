import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.html': 'text/html; charset=utf-8',
        '.css': 'text/css; charset=utf-8',
        '.js': 'text/javascript; charset=utf-8',
        '.json': 'application/json',
        '.jpg': 'image/jpeg',
        '.png': 'image/png',
        '.svg': 'image/svg+xml',
    }

with socketserver.TCPServer(("127.0.0.1", 5500), Handler) as httpd:
    print("Serving at http://127.0.0.1:5500")
    httpd.serve_forever()
