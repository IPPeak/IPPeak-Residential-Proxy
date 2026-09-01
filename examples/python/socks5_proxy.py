import requests

PROXY_HOST = "HOST"
PROXY_PORT = "PORT"
PROXY_USERNAME = "USERNAME"
PROXY_PASSWORD = "PASSWORD"

proxy = (
    f"socks5h://{PROXY_USERNAME}:{PROXY_PASSWORD}"
    f"@{PROXY_HOST}:{PROXY_PORT}"
)

proxies = {
    "http": proxy,
    "https": proxy,
}

target_url = "https://httpbin.org/ip"

try:
    response = requests.get(
        target_url,
        proxies=proxies,
        timeout=30
    )

    response.raise_for_status()

    print("SOCKS5 proxy request successful!")
    print("IP response:")
    print(response.text)

except requests.RequestException as error:
    print(f"Request failed: {error}")
