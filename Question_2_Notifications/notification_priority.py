import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
import requests
from logger import get_auth_token

def process():
    url = "http://4.224.186.213/evaluation-service/notifications"
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code != 200: return
    
    data = r.json().get("notifications", [])
    
    def key(item):
        weights = {"placement": 3, "result": 2, "event": 1}
        w = weights.get(item["Type"].lower(), 0)
        t = datetime.strptime(item["Timestamp"], "%Y-%m-%d %H:%M:%S")
        return (w, t)
        
    data.sort(key=key, reverse=True)
    for entry in data[:10]:
        print(f"{entry['Type']} - {entry['Message']}")

if __name__ == "__main__":
    process()