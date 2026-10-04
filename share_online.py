import subprocess
import re
import time
import sys
import os
import urllib.request

# Ensure UTF-8 output encoding on Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if sys.platform == 'win32':
    CLOUDFLARED_PATH = os.path.join(BASE_DIR, "cloudflared.exe")
else:
    CLOUDFLARED_PATH = os.path.join(BASE_DIR, "cloudflared")
MANAGE_PY = os.path.join(BASE_DIR, "manage.py")

print("=" * 65)
print("     🚀 ĐANG KHỞI ĐỘNG HỆ THỐNG PHÁT SÓNG ONLINE TUTORLINK")
print("=" * 65)

# 1. Kiểm tra máy chủ Django (cổng 8080 hoặc 8000)
def check_port(port):
    try:
        req = urllib.request.urlopen(f"http://127.0.0.1:{port}", timeout=1.5)
        return True
    except Exception:
        return False

target_port = None
django_proc = None

if check_port(8080):
    target_port = 8080
    print("[✓] Phát hiện Django đang chạy sẵn trên cổng 8080.")
elif check_port(8000):
    target_port = 8000
    print("[✓] Phát hiện Django đang chạy sẵn trên cổng 8000.")
else:
    target_port = 8000
    print("[*] Đang khởi động máy chủ Django trên cổng 8000...")
    django_proc = subprocess.Popen(
        [sys.executable, MANAGE_PY, "runserver", "0.0.0.0:8000"],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    for _ in range(15):
        time.sleep(1)
        if check_port(8000):
            print("[✓] Máy chủ Django đã khởi động thành công trên cổng 8000.")
            break
    else:
        print("[!] Lưu ý: Máy chủ Django đang khởi động chậm, tiếp tục tạo link...")

# 2. Kiểm tra file cloudflared.exe
if not os.path.exists(CLOUDFLARED_PATH):
    print(f"[-] Lỗi: Không tìm thấy file {CLOUDFLARED_PATH}")
    sys.exit(1)

# 3. Tạo Cloudflare Tunnel đến cổng đang chạy
print(f"[*] Đang kết nối Cloudflare tới máy chủ (cổng {target_port}) để tạo link an toàn...")
cf_proc = subprocess.Popen(
    [CLOUDFLARED_PATH, "tunnel", "--url", f"http://127.0.0.1:{target_port}"],
    cwd=BASE_DIR,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

tunnel_url = None
start_time = time.time()
while time.time() - start_time < 30:
    line = cf_proc.stdout.readline()
    if not line:
        time.sleep(0.1)
        continue
    match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
    if match:
        tunnel_url = match.group(0)
        break

if tunnel_url:
    try:
        if sys.platform == 'darwin':
            p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            p.communicate(tunnel_url.encode('utf-8'))
            clipboard_note = "(Đã tự động COPY link vào bộ nhớ tạm, bạn chỉ việc Cmd + V để gửi)"
        else:
            subprocess.run(["powershell", "-Command", f"Set-Clipboard -Value '{tunnel_url}'"], check=False)
            clipboard_note = "(Đã tự động COPY link vào bộ nhớ tạm, bạn chỉ việc Ctrl + V để gửi)"
    except Exception:
        clipboard_note = ""

    print("\n" + "=" * 65)
    print(" 🎉 ĐÃ TẠO LINK TRUY CẬP THÀNH CÔNG CHO NGƯỜI KHÁC VÀO!")
    print(f" 👉 LINK: {tunnel_url}")
    if clipboard_note:
        print(f" 📋 {clipboard_note}")
    print("=" * 65)
    print("\n💡 THÔNG TIN KIỂM THỬ / ĐĂNG NHẬP:")
    print(" • Tài khoản Admin:    admin / admin123")
    print(" • Tài khoản Học sinh: hocsinh1 / 123456")
    print(" • Tài khoản Gia sư:   giasu_toan / 123456")
    print("\n[*] LƯU Ý QUAN TRỌNG:")
    print(" - Bất kỳ ai ở bất kỳ đâu (Wifi, 4G, điện thoại, máy tính) đều vào được.")
    print(" - Cửa sổ này phải ĐƯỢC GIỮ MỞ để duy trì link.")
    print(" - Khi bạn ĐÓNG CỬA SỔ hoặc nhấn Ctrl + C, link sẽ tự động hủy.")
    print("=" * 65 + "\n")

    try:
        # Giữ tiến trình chạy cho đến khi người dùng ngắt
        while True:
            time.sleep(1)
            if cf_proc.poll() is not None:
                print("[-] Cloudflare tunnel đã ngắt kết nối.")
                break
    except KeyboardInterrupt:
        print("\n[*] Đang tắt hệ thống phát sóng...")
    finally:
        try:
            cf_proc.terminate()
        except Exception:
            pass
        if django_proc:
            try:
                django_proc.terminate()
            except Exception:
                pass
        print("[✓] Đã ngắt link và dọn dẹp tiến trình an toàn.")
else:
    print("[-] Không thể lấy được đường link sau 30 giây. Vui lòng kiểm tra lại kết nối mạng Internet.")
    if django_proc:
        django_proc.terminate()

