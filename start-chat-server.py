import http.server
import socketserver
import os
import sys

PORT = 8765
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def get_local_ip():
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == "__main__":
    local_ip = get_local_ip()
    
    print(f"=" * 50)
    print(f"LM Studio Chat 服务器已启动")
    print(f"=" * 50)
    print(f"本机访问: http://localhost:{PORT}/lmstudio-chat.html")
    print(f"网络访问: http://{local_ip}:{PORT}/lmstudio-chat.html")
    print(f"=" * 50)
    print(f"其他设备请访问上面的'网络访问'地址")
    print(f"按 Ctrl+C 停止服务器")
    print(f"=" * 50)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")
            httpd.shutdown()