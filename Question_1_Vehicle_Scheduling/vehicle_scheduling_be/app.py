import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests
from logger import log_event, get_auth_token

def fetch_data(url):
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    return None

def solve(max_hours, items):
    n = len(items)
    dp = [[0] * (max_hours + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d = items[i-1]["Duration"]
        imp = items[i-1]["Impact"]
        for w in range(max_hours + 1):
            if d <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-d] + imp)
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][max_hours]

def main():
    log_event("backend", "info", "controller", "init")
    d_data = fetch_data("http://4.224.186.213/evaluation-service/depots")
    v_data = fetch_data("http://4.224.186.213/evaluation-service/vehicles")
    if not d_data or not v_data:
        log_event("backend", "fatal", "db", "error")
        return
    for d in d_data.get("depots", []):
        imp = solve(d["MechanicHours"], v_data.get("vehicles", []))
        log_event("backend", "info", "service", f"depot {d['ID']} impact {imp}")

if __name__ == "__main__":
    main()