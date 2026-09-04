---
layout: default
title: API Reference
---

# API Reference


This section explains how to integrate IPPeak proxy services into your applications.


IPPeak provides standard proxy access methods compatible with common HTTP clients, automation tools, and custom applications.



---

# API Overview


IPPeak proxy infrastructure supports:


- HTTP proxy connections
- HTTPS proxy connections
- SOCKS5 proxy connections
- Authentication-based access
- Multiple programming languages



---

# Authentication


All proxy requests require authentication.


Authentication credentials include:


```
Username
Password
Host
Port
```



Example:


```
Username: your_username

Password: your_password

Host: proxy.example.com

Port: 8080
```



---

# Proxy Endpoint


The standard proxy format:


```
protocol://username:password@host:port
```


Example:


```
http://username:password@proxy.example.com:8080
```



For SOCKS5:


```
socks5://username:password@proxy.example.com:1080
```



---

# Connection Parameters


| Parameter | Description |
|---|---|
| Host | Proxy server address |
| Port | Proxy connection port |
| Username | Authentication username |
| Password | Authentication password |
| Protocol | HTTP / HTTPS / SOCKS5 |



---

# HTTP Request Example


Example request:


```http
GET https://example.com HTTP/1.1

Host: example.com

Proxy-Authorization: Basic authentication
```



---

# Python Example


Install dependency:


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
    "https://example.com",
    proxies=proxy,
    timeout=30
)


print(response.status_code)
```



---

# Node.js Example


Install dependency:


```bash
npm install axios
```



Example:


```javascript
const axios = require("axios");


axios.get(
    "https://example.com",
    {
        proxy:{
            host:"proxy.example.com",
            port:8080,
            auth:{
                username:"username",
                password:"password"
            }
        }
    }
)
.then(response=>{
    console.log(response.status);
});
```



---

# Go Example


Example:


```go
package main


import (
    "fmt"
    "net/http"
    "net/url"
)


func main(){

    proxyURL, _ := url.Parse(
        "http://username:password@host:port",
    )


    client := &http.Client{
        Transport:&http.Transport{
            Proxy:http.ProxyURL(proxyURL),
        },
    }


    response, _ := client.Get(
        "https://example.com",
    )


    fmt.Println(response.Status)
}
```



---

# Error Handling


Common connection issues:



## Authentication Failed


Possible reasons:


- Incorrect username
- Incorrect password
- Expired credentials



## Connection Timeout


Check:


- Proxy host
- Port configuration
- Network connection



## Invalid Proxy Format


Make sure your proxy follows:


```
protocol://username:password@host:port
```



---

# Best Practices


## Use Connection Sessions


For applications requiring stable access, use appropriate session settings.



## Handle Errors


Implement retry and timeout logic.



## Choose The Right Proxy Type


Select the proxy solution based on your application requirements.


---

# Next Steps


Continue learning:


- [Getting Started](getting-started.md)
- [Proxy Types](proxy-types.md)
- [Code Examples](examples/python.html)
