---
layout: default
title: Code Examples
---

# Code Examples


IPPeak provides ready-to-use examples for developers who want to quickly integrate proxy connections into their applications.


The examples repository includes common programming languages and different proxy connection methods.



---

# Python Examples


Python examples demonstrate how to connect IPPeak proxies using the requests library.


Location:


```
examples/python/
```



---

## Rotating Proxy


File:


```
rotating_proxy.py
```


Use cases:


- General proxy requests
- Data collection
- Applications requiring IP rotation


Example:


```python
import requests


proxy = {
    "http": "http://username:password@host:port",
    "https": "http://username:password@host:port"
}


response = requests.get(
    "https://example.com",
    proxies=proxy
)


print(response.text)
```



---

## Sticky Session Proxy


File:


```
sticky_session.py
```


Use cases:


- Maintain the same IP during a session
- Long-running requests
- Session-based applications



---

## SOCKS5 Proxy


File:


```
socks5_proxy.py
```


Use cases:


- SOCKS5 compatible applications
- Custom network clients



---

# Go Example


Location:


```
examples/go/
```


File:


```
main.go
```


The Go example demonstrates how to configure HTTP proxy connections using the standard Go HTTP client.



---

# Node.js Example


Location:


```
examples/nodejs/
```


File:


```
proxy_demo.js
```


The Node.js example shows how to integrate IPPeak proxy services with JavaScript applications.



---

# Running Examples


Before running examples:


1. Install required dependencies


2. Replace proxy credentials:


```
username
password
host
port
```


3. Run the example program



---

# Example Repository Structure


```
examples

├── python

│   ├── rotating_proxy.py

│   ├── sticky_session.py

│   └── socks5_proxy.py


├── go

│   └── main.go


└── nodejs

    └── proxy_demo.js
```



---

# Next Steps


Continue learning:


- [Getting Started](getting-started.md)
- [Proxy Types](proxy-types.md)
- [API Reference](api.md)
