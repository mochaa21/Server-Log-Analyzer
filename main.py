import json
import time
from typing import Callable

# Data simulasi dari server (berwujud String JSON)
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

# TUGAS 1: Buat Decorator
# Buat decorator bernama @timer_decorator yang mencetak "Memproses data..." 
# sebelum fungsi berjalan, dan "Proses selesai!" setelah fungsi selesai.
def timer_decorator(func):
    def myinner():
        print("Processing Data")
        time.sleep(2.5)
        print("Process Complete!")
        return
    return myinner


# TUGAS 2, 3, & 4: Fungsi Utama dengan Type Annotations
# Buat fungsi analyze_logs yang menerima argumen string dan mereturn list.
# Jangan lupa pakaikan jaket @timer_decorator di atasnya.
def analyze_logs(data):
    response = json.loads(raw_api_response)
    node_1 = response['data']['node_1_logins']
    node_2 = response['data']['node_2_logins']
    banned_users = response['data']['banned_users']
    dataset_1 = set(int(angka) for angka in node_1.strip().split(', '))
    dataset_2 = set(int(angka) for angka in node_2.strip().split(', '))
    new_data = dataset_1.intersection(dataset_2)
    new_data_check = new_data.difference(banned_users)
    complete_data = list(new_data_check)
    return complete_data

analyze_logs(raw_api_response)


# --- EKSEKUSI ---
# Panggil fungsi analyze_logs dengan memasukkan raw_api_response
# Cetak hasil akhirnya. 
# Ekspektasi Output Terminal: 
# Memproses data...
# Proses selesai!
# Pemain valid yang aktif di kedua node: [105, 305]