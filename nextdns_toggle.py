import requests
import os

# Thông tin cấu hình
NEXTDNS_PROFILE_ID = os.getenv("NEXTDNS_PROFILE_ID")  # ID Profile NextDNS
API_KEY = os.getenv("NEXTDNS_API_KEY")  # API Key NextDNS
DOMAINS_TO_TOGGLE = ["puffer.6.1945015797.kgvn.gcloud.garena.vn",
    "itop.kg.garena.vn",
    "garena.com",
    "garena.vn",
    "dl.ops.kgvn.garenanow.com"]

# URL API NextDNS
BASE_URL = f"https://api.nextdns.io/profiles/{NEXTDNS_PROFILE_ID}/denylist"

# Headers API
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def get_current_denylist():
    """Lấy danh sách domain hiện đang bị chặn"""
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Lỗi khi lấy danh sách Denylist: {response.status_code}, {response.text}")
        return []

def toggle_domain(domain):
    """Bật/Tắt chặn domain dựa vào trạng thái hiện tại"""
    denylist = get_current_denylist()

    if domain in denylist:
        # Nếu domain đã bị chặn, thì xóa nó khỏi Denylist (Tắt chặn)
        response = requests.delete(f"{BASE_URL}/{domain}", headers=HEADERS)
        action = "TẮT chặn"
    else:
        # Nếu domain chưa bị chặn, thì thêm nó vào Denylist (Bật chặn)
        response = requests.put(f"{BASE_URL}/{domain}", headers=HEADERS)
        action = "BẬT chặn"

    if response.status_code in [200, 204]:
        print(f"{action} thành công: {domain}")
    else:
        print(f"Lỗi khi {action} {domain}: {response.status_code}, {response.text}")

if __name__ == "__main__":
    for domain in DOMAINS_TO_TOGGLE:
        toggle_domain(domain)
