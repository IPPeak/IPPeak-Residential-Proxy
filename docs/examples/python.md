---
layout: default
title: Python Examples
---

# Python Examples


This guide shows how to integrate IPPeak proxy services with Python applications.


The examples use the Python `requests` library to create proxy connections.



---

# Requirements


Before running the examples, install:


```bash
pip install requests
```



You will need:


```
Proxy Host
Proxy Port
Username
Password
```



---

# Rotating Proxy Example


Rotating proxies automatically switch IP addresses based on your session settings.


File:


```
examples/python/rotating_proxy.py
```



Example:


```python
import requests


proxy = {
    "http": "http://username:password@host:port",
    "https": "http://username:password@host:port"
}


response = requests.get(
    "https://example.com",
    proxies=proxy,
    timeout=30
)


print(response.text)
```



---

# Sticky Session Example


Sticky sessions allow requests to maintain the same IP address during a session.



File:


```
examples/python/sticky_session.py
```



Recommended for:


- Account sessions
- Long-running requests
- Applications requiring IP consistency



---

# SOCKS5 Proxy Example


SOCKS5 proxy connections are suitable for applications requiring SOCKS-compatible networking.



File:


```
examples/python/socks5_proxy.py
```



Example:


```python
import requests


proxies = {
    "http": "socks5://username:password@host:port",
    "https": "socks5://username:password@host:port"
}


response = requests.get(
    "https://example.com",
    proxies=proxies
)


print(response.status_code)
```



---

# Running The Example


1. Clone the repository:


```
git clone https://github.com/IPPeak/IPPeak-Residential-Proxy.git
```


2. Install dependencies:


```
pip install requests
```


3. Replace proxy credentials.


4. Run the Python file.


Example:


```
python rotating_proxy.py
```



---

# More Examples


Explore examples in other programming languages:


- [Python Examples](python/)

- [Go Examples](go/)

- [Node.js Examples](nodejs/)



---

# Related Documentation


- [Getting Started](../getting-started.md)

- [Proxy Types](../proxy-types.md)

- [API Reference](../api.md)
