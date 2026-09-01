import requests

PROXY_HOST = "HOST"
PROXY_PORT = "PORT"
PROXY_USERNAME = "USERNAME"
PROXY_PASSWORD = "PASSWORD"

SESSION_ID = "session123"

proxy_username = f"{PROXY_USERNAME}-session-{SESSION_ID}"

proxy = (
    f"http://{proxy_username}:{PROXY_PASSWORD}"
    f"@{PROXY_HOST}:{PROXY_PORT}"
)

proxies = {
    "http": proxy,
    "https": proxy,
}

target_url = "https://httpbin.org/ip"

session = requests.Session()
session.proxies.update(proxies)

try:
    for i in range(3):
        response = session.get(
            target_url,
            timeout=30
        )

        response.raise_for_status()

        print(f"Request {i + 1}:")
        print(response.text)

except requests.RequestException as error:
    print(f"Request failed: {error}")
