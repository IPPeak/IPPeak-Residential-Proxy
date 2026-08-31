import requests

proxy = "http://USERNAME:PASSWORD@HOST:PORT"

proxies = {
    "http": proxy,
    "https": proxy,
}

response = requests.get(
    "https://httpbin.org/ip",
    proxies=proxies,
    timeout=30
)

print(response.text)
