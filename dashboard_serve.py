#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生产数据看板 - 跨平台本地静态服务器
用法：把此脚本和"生产数据看板_独立版.html"放在同目录，python3 dashboard_serve.py
端口 8090，浏览器打开 http://127.0.0.1:8090/dashboard.html
"""
import http.server
import os
import socketserver
import sys
import threading
import webbrowser

PORT = 8090
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_NAME = "生产数据看板_独立版.html"
DASH_NAME = "dashboard.html"


def ensure_dashboard():
    """首次启动时把独立版复制为 ASCII 名（避免 URL 中文编码）"""
    src = os.path.join(SCRIPT_DIR, INDEX_NAME)
    dst = os.path.join(SCRIPT_DIR, DASH_NAME)
    if not os.path.exists(src):
        print(f"[错误] 当前目录没有 {INDEX_NAME}")
        print(f"       请把脚本放到独立版 HTML 同目录下。")
        sys.exit(1)
    if not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst):
        import shutil
        shutil.copy2(src, dst)
        print(f"[OK] 复制 {INDEX_NAME} → {DASH_NAME}")


def kill_old_listener():
    """尝试杀掉占用 8090 的旧进程（Windows only）"""
    if os.name != "nt":
        return
    try:
        import subprocess
        out = subprocess.check_output(
            f'netstat -ano | findstr ":{PORT}" | findstr LISTENING',
            shell=True, text=True
        )
        for line in out.strip().splitlines():
            parts = line.split()
            if len(parts) >= 5:
                pid = parts[-1]
                subprocess.run(f'taskkill /F /PID {pid}', shell=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"[OK] 已停止占用 {PORT} 的旧进程 (PID={pid})")
    except Exception:
        pass


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=SCRIPT_DIR, **kw)

    def log_message(self, fmt, *args):
        # 静默常规访问日志
        pass


def open_browser():
    """延迟 1 秒后开浏览器"""
    import time
    time.sleep(1)
    webbrowser.open(f"http://127.0.0.1:{PORT}/dashboard.html")


def main():
    os.chdir(SCRIPT_DIR)
    print("=" * 60)
    print(f" 生产数据看板 - 本地服务")
    print(f" 端口: {PORT}")
    print(f" 看板: http://127.0.0.1:{PORT}/dashboard.html")
    print(f" 关闭此窗口即停止服务")
    print("=" * 60)
    kill_old_listener()
    ensure_dashboard()
    threading.Thread(target=open_browser, daemon=True).start()
    try:
        with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as srv:
            print(f"[OK] 服务启动成功，按 Ctrl+C 停止")
            srv.serve_forever()
    except KeyboardInterrupt:
        print("\n[OK] 已停止")
    except OSError as e:
        print(f"[错误] 端口 {PORT} 启动失败：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
