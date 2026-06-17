import requests

CLIENT_ID = "10e240e4-50b9-490c-964e-1eda0ffe7e54"
CLIENT_SECRET = "kPnxFNXNMPHCSmHt"
AUTH_URL = "http://4.224.186.213/evaluation-service/auth"
LOG_URL = "http://4.224.186.213/evaluation-service/logs"

def get_auth_token():
    payload = {
        "email": "nmdsuhail17@gmail.com",
        "name": "Mohamed Suhail N",
        "rollNo": "12956",
        "accessCode": "juFphv",
        "clientID": CLIENT_ID,
        "clientSecret": CLIENT_SECRET
    }
    response = requests.post(AUTH_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("access_token")
    return None

def log_event(stack, level, package, message):
    token = get_auth_token()
    if not token:
        return
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "stack": stack.lower(),
        "level": level.lower(),
        "package": package.lower(),
        "message": message
    }
    requests.post(LOG_URL, json=payload, headers=headers)
