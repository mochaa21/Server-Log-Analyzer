import json
import time
import functools
from typing import Callable

raw_api_response = """
{
    "status": "success",
    "data": {
        "node_1_logins": " 101, 105, 101, 204, 305 ",
        "node_2_logins": " 305, 204, 105, 105, 400 ",
        "banned_users": ["204"]
    }
}
"""

def timer_decorator(func: callable) -> callable:
    @functools.wraps(func)
    def myinner(*args, **kwargs):
        print("Processing Data...")
        time.sleep(2.5)
        hasil = func(*args, **kwargs)
        print("Process Complete!")
        return hasil
    return myinner

@timer_decorator
def analyze_logs(data: str) -> str:
    response: dict = json.loads(raw_api_response)
    node_1: str = response['data']['node_1_logins']
    node_2: str = response['data']['node_2_logins']
    banned_users: list = response['data']['banned_users']
    dataset_1: set = set(int(angka) for angka in node_1.strip().split(', '))
    dataset_2: set = set(int(angka) for angka in node_2.strip().split(', '))
    list_banned: set = set(int(angka) for angka in banned_users)
    new_data: set = dataset_1.intersection(dataset_2)
    new_data_check: set = new_data.difference(list_banned)
    complete_data: list = sorted(new_data_check)
    return f"Valid players active on both nodes: {complete_data}"

print(analyze_logs(raw_api_response))


# --- EKSEKUSI ---
# Panggil fungsi analyze_logs dengan memasukkan raw_api_response
# Cetak hasil akhirnya. 
# Ekspektasi Output Terminal: 
# Memproses data...
# Proses selesai!
# Pemain valid yang aktif di kedua node: [105, 305]