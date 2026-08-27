import http.server
import socketserver
import os
import sys

PORT = 8765
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def get_all_local_ips():
    """获取所有可用的本地局域网 IP 地址"""
    import socket
    ips = set()
    
    # 方法1: 通过 socket 连接获取主网卡 IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        if not ip.startswith('127.') and not ip.startswith('169.254.'):
            ips.add(ip)
        s.close()
    except Exception:
        pass
    
    # 方法2: 遍历所有网络接口
    try:
        hostname = socket.gethostname()
        addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET)
        for info in addr_info:
            ip = info[4][0]
            if not ip.startswith('127.') and not ip.startswith('169.254.'):
                ips.add(ip)
    except Exception:
        pass
    
    # 方法3: 使用 psutil 或 netifaces（可选依赖）
    try:
        import netifaces
        for interface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(interface).get(netifaces.AF_INET, [])
            for addr in addrs:
                ip = addr.get('addr', '')
                if ip and not ip.startswith('127.') and not ip.startswith('169.254.'):
                    ips.add(ip)
    except Exception:
        pass
    
    return list(ips) if ips else ["127.0.0.1"]

def get_local_ip():
    """获取主局域网 IP（兼容旧版本）"""
    ips = get_all_local_ips()
    # 优先返回非回环地址
    for ip in ips:
        if not ip.startswith('127.') and not ip.startswith('169.254.'):
            return ip
    return ips[0] if ips else "127.0.0.1"

if __name__ == "__main__":
    local_ips = get_all_local_ips()
    main_ip = get_local_ip()
    
    print(f"=" * 50)
    print(f"LLM Chat Bridge v1.2.0 服务器已启动")
    print(f"=" * 50)
    print(f"本机访问: http://localhost:{PORT}/lmstudio-chat.html")
    
    if len(local_ips) > 1:
        print(f"\n可用网络地址:")
        for i, ip in enumerate(local_ips, 1):
            print(f"  {i}. http://{ip}:{PORT}/lmstudio-chat.html")
    else:
        print(f"网络访问: http://{main_ip}:{PORT}/lmstudio-chat.html")
        
    print(f"\n其他设备请访问上面的地址")
    print(f"按 Ctrl+C 停止服务器")
    print(f"=" * 50)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        # 允许端口重用
        httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")
            httpd.shutdown()
