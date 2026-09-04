---
layout: default
title: Getting Started
---

# Getting Started


This guide explains how to connect to IPPeak proxy services and make your first successful proxy request.


IPPeak provides residential proxy solutions with global IP coverage, multiple proxy protocols, and flexible integration options.


---

# Before You Start


Before connecting to IPPeak proxies, make sure you have:


- An active IPPeak account
- Proxy username
- Proxy password
- Proxy host
- Proxy port


These credentials are required for proxy authentication.



---

# Step 1: Get Proxy Credentials


After purchasing or activating a proxy service, you will receive connection information.


A typical proxy configuration includes:


```
Host:
Port:
Username:
Password:
```


Example:


```
Host: proxy.example.com

Port: 8080

Username: your_username

Password: your_password
```



---

# Step 2: Proxy Connection Format


IPPeak supports standard proxy authentication formats.


## HTTP Proxy


Format:


```
http://username:password@host:port
```


Example:


```
http://user123:pass123@proxy.example.com:8080
```



## SOCKS5 Proxy


Format:


```
socks5://username:password@host:port
```


Example:


```
socks5://user123:pass123@proxy.example.com:1080
```



---

# Step 3: Send Your First Request


## Python Example


Install requests:


```bash
pip install requests
```


Example:


```python
import requests


proxy = {
    "http": "http://username:password@host:port",
    "https": "http://username:password@host:port"
}


response = requests.get(
    "https://ipinfo.io",
    proxies=proxy,
    timeout=30
)


print(response.text)
```



---

# Step 4: Verify Your Connection


After sending a request, you can verify your proxy connection by checking:


- IP address
- Country location
- Network information


Example verification service:


```
https://ipinfo.io
```



A successful response should display the proxy IP information instead of your original network IP.



---

# Supported Proxy Protocols


IPPeak supports:


| Protocol | Supported |
|---|---|
| HTTP | Yes |
| HTTPS | Yes |
| SOCKS5 | Yes |



---

# Connection Tips


## Use Session Control


For applications requiring consistent IP addresses, use sticky sessions.


## Manage Request Frequency


Avoid sending excessive requests from a single IP address.


## Select The Right Proxy Type


Choose the proxy solution based on your application requirements.


---

# Next Steps


Continue exploring IPPeak documentation:


- [Proxy Types](proxy-types.md)
- [API Reference](api.md)
- [Code Examples](examples/python.html)
