#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import argparse

class PutGetHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        path = self.path.lstrip("/")
        length = int(self.headers['Content-Length'])
        with open(path, 'wb') as output_file:
            output_file.write(self.rfile.read(length))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"\033[92mUpload complete.\n\033[0m")

    def do_GET(self):
        path = self.path.lstrip("/")
        if os.path.exists(path):
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.end_headers()
            with open(path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"\033[91mFile not found.\n\033[0m")

def main():
    parser = argparse.ArgumentParser(description="🌀 TunchiTools - Minimalist PUT/GET HTTP server")
    parser.add_argument('--port', type=int, default=8000, help='Port to listen on (default: 8000)')
    args = parser.parse_args()

    banner = r"""
 ________                            __       __ ________                   __          
|        \                          |  \     |  \        \                 |  \         
 \▓▓▓▓▓▓▓▓__    __ _______   _______| ▓▓____  \▓▓\▓▓▓▓▓▓▓▓ ______   ______ | ▓▓ _______ 
   | ▓▓  |  \  |  \       \ /       \ ▓▓    \|  \  | ▓▓   /      \ /      \| ▓▓/       \
   | ▓▓  | ▓▓  | ▓▓ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓\ ▓▓  | ▓▓  |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓  ▓▓▓▓▓▓▓
   | ▓▓  | ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓  | ▓▓  | ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓\▓▓    \ 
   | ▓▓  | ▓▓__/ ▓▓ ▓▓  | ▓▓ ▓▓_____| ▓▓  | ▓▓ ▓▓  | ▓▓  | ▓▓__/ ▓▓ ▓▓__/ ▓▓ ▓▓_\▓▓▓▓▓▓\
   | ▓▓   \▓▓    ▓▓ ▓▓  | ▓▓\▓▓     \ ▓▓  | ▓▓ ▓▓  | ▓▓   \▓▓    ▓▓\▓▓    ▓▓ ▓▓       ▓▓
    \▓▓    \▓▓▓▓▓▓ \▓▓   \▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓\▓▓   \▓▓    \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓\▓▓▓▓▓▓▓ 
                                                                                                                                              
             🚀  TunchiTools — PUT/GET Server
    """
    print(f"\033[96m{banner}\033[0m")
    print(f"\033[94m[+] Server running on port {args.port} (0.0.0.0)\033[0m")
    print("\033[93m[!] Upload via PUT or download via GET\n\033[0m")

    print("\033[92m[+] Example PUT Requests:\033[0m")
    print("\033[90mLinux:\033[0m   curl -T ./file.txt http://<host>:<port>/file.txt")
    print("\033[90mWindows:\033[0m $wc = New-Object System.Net.WebClient; $wc.UploadFile('http://<host>:<port>/file.txt','PUT','C:\\path\\to\\file.txt')\n")

    server = HTTPServer(('0.0.0.0', args.port), PutGetHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Server stopped by user.\033[0m")


if __name__ == '__main__':
    main()
