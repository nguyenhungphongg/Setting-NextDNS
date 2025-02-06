import requests
import os

# Thông tin cấu hình
NEXTDNS_PROFILE_ID = os.getenv("NEXTDNS_PROFILE_ID")  # ID Profile NextDNS
API_KEY = os.getenv("NEXTDNS_API_KEY")  # API Key NextDNS
BLOCKLIST_ID = "custom-blocklist"  # ID của blocklist cần chỉnh sửa
DOMAIN_TO_BLOCK = "facebook.com"  # Domain cần chặn

# Hàm bật/tắt domain
def toggle_blocklist(enable: bool):
    url = f"https://api.nextdns.io/profiles/{NEXTDNS_PROFILE_ID}/denylist/{DOMAIN_TO_BLOCK}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    if enable:
        response = requests.put(url, headers=headers)  # Thêm vào blocklist
    else:
        response = requests.delete(url, headers=headers)  # Xóa khỏi blocklist

    if response.status_code in [200, 204]:
        print(f"Đã {'bật' if enable else 'tắt'} chặn {DOMAIN_TO_BLOCK}")
    else:
        print(f"Lỗi: {response.status_code}, {response.text}")

# Chạy script
if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "enable"
    toggle_blocklist(action == "enable")
