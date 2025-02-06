import requests
import os

# Thông tin cấu hình
NEXTDNS_PROFILE_ID = os.getenv("25be1f")  # ID Profile NextDNS
API_KEY = os.getenv("c4c33952dbe4347593c86de6392f5c533e394707")  # API Key NextDNS

# Danh sách domain cần chặn/mở
DOMAINS_TO_BLOCK = [
    "puffer.6.1945015797.kgvn.gcloud.garena.vn",
    "itop.kg.garena.vn",
    "garena.com",
    "garena.vn",
    "dl.ops.kgvn.garenanow.com"
]

# Hàm bật/tắt domain
def toggle_blocklist(enable: bool):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    for domain in DOMAINS_TO_BLOCK:
        url = f"https://api.nextdns.io/profiles/{NEXTDNS_PROFILE_ID}/denylist/{domain}"
        
        if enable:
            response = requests.put(url, headers=headers)  # Thêm vào blocklist
        else:
            response = requests.delete(url, headers=headers)  # Xóa khỏi blocklist

        if response.status_code in [200, 204]:
            print(f"Đã {'bật' if enable else 'tắt'} chặn {domain}")
        else:
            print(f"Lỗi {response.status_code} khi xử lý {domain}: {response.text}")

# Chạy script
if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "enable"
    toggle_blocklist(action == "enable")
