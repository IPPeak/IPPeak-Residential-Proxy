---
layout: default
title: "How to Configure a Proxy with Python Requests? A Complete Guide"
description: "Learn how to configure HTTP, HTTPS, and SOCKS5 proxies with Python Requests, including authentication, Sessions, rotating residential proxies, and common proxy issues."
---

# How to Configure a Proxy with Python Requests? A Complete Guide

Python Requests is a widely used HTTP library for sending web requests. In data collection, API testing, and automation tasks, developers may need to route requests through a proxy server.

Requests supports proxy configuration through the `proxies` parameter. This guide explains how to configure HTTP, HTTPS, and SOCKS5 proxies, use authenticated proxies, manage Sessions, and work with rotating residential proxies.

## 1. Install Requests

If Requests is not installed yet, run:

```text
pip install requests
```

Then import it into your Python script:

```text
import requests
```

## 2. Configure a Basic Proxy

Requests allows you to specify a proxy through the `proxies` parameter.

For example:

```text
import requests

proxies = {
    "http": "http://proxy.example.com:8080",
    "https": "http://proxy.example.com:8080"
}

response = requests.get(
    "https://httpbin.org/ip",
    proxies=proxies,
    timeout=10
)

print(response.text)
```

The `http` and `https` entries define which proxy should be used for each type of request.

Keep in mind that the proxy protocol depends on the proxy service being used. An HTTPS request does not necessarily require an `https://` proxy URL.

## 3. Configure an Authenticated Proxy

If the proxy requires authentication, the username and password can be included in the proxy URL:

```text
proxies = {
    "http": "http://username:password@proxy.example.com:8080",
    "https": "http://username:password@proxy.example.com:8080"
}

response = requests.get(
    "https://httpbin.org/ip",
    proxies=proxies,
    timeout=10
)

print(response.text)
```

For production projects, avoid storing usernames and passwords directly in publicly accessible source code. Environment variables or other secure configuration methods are better options.

## 4. Use a SOCKS5 Proxy

Requests primarily supports HTTP proxies by default. To use SOCKS5, additional SOCKS support needs to be installed:

```text
pip install requests[socks]
```

Then configure the proxy:

```text
proxies = {
    "http": "socks5://127.0.0.1:1080",
    "https": "socks5://127.0.0.1:1080"
}

response = requests.get(
    "https://httpbin.org/ip",
    proxies=proxies,
    timeout=10
)

print(response.text)
```

If the proxy service supports remote DNS resolution, `socks5h` can also be used so that DNS requests are resolved through the proxy.

## 5. Reuse Proxy Settings with Session

When an application needs to send multiple requests, `requests.Session()` can be used to manage the proxy configuration:

```text
session = requests.Session()

session.proxies.update({
    "http": "http://username:password@proxy.example.com:8080",
    "https": "http://username:password@proxy.example.com:8080"
})

response = session.get(
    "https://httpbin.org/ip",
    timeout=10
)

print(response.text)
```

Using a Session avoids repeating the proxy configuration for every request and makes it easier to manage shared request settings.

## 6. Using Rotating Residential Proxies

For applications that send multiple requests and need different residential IPs, Rotating Residential Proxies can be an option.

These proxies generally provide a proxy endpoint through which IP rotation is managed by the proxy service. The developer only needs to configure the proxy endpoint in Requests.

For example:

```text
proxies = {
    "http": "http://username:password@proxy.example.com:8080",
    "https": "http://username:password@proxy.example.com:8080"
}

for url in urls:
    response = requests.get(
        url,
        proxies=proxies,
        timeout=10
    )

    print(response.status_code)
```

The actual rotation behavior depends on the proxy provider and Session configuration. Some services can assign a different IP for each request, while others allow the same IP to remain active for a defined Session period.

If consecutive requests need to use the same IP, a Sticky Session can be more suitable. If requests require different IPs, a Rotating Session may be preferable.

## 7. IPPeak Residential Proxies

For developers using Python Requests for data collection, automation, or other network tasks, IPPeak Residential Proxies provide residential proxy resources that can be integrated with standard Requests configurations.

IPPeak provides **80M+ real residential IPs** across **195+ countries and regions**, with support for **HTTP & SOCKS5**. Its Residential Proxies support both **Rotating Sessions and Sticky Sessions**, allowing developers to choose a Session type based on their application requirements.

For example, Requests can be configured using the proxy host, port, and authentication information provided by IPPeak:

```text
import requests

proxies = {
    "http": "http://USERNAME:PASSWORD@HOST:PORT",
    "https": "http://USERNAME:PASSWORD@HOST:PORT"
}

response = requests.get(
    "https://httpbin.org/ip",
    proxies=proxies,
    timeout=10
)

print(response.text)
```

If different requests need to use different IPs, a Rotating Session can be selected. If the same IP needs to remain active for a period of time, a Sticky Session can be used instead.

IPPeak Residential Proxies also support high-concurrency connections, making them suitable for applications that need to handle multiple requests concurrently.

## 8. How to Choose a Proxy for Requests

When selecting a proxy for a Python Requests project, consider the following factors:

**Proxy Protocol**

Check whether the proxy supports HTTP or SOCKS5 and whether it is compatible with your application.

**IP Type**

Choose the IP type according to the requirements of your project. Residential Proxies can be considered when a residential network environment is needed, while Static Residential Proxies can be useful when a long-term dedicated IP is required.

**Session Type**

Use a Sticky Session when consecutive requests need to maintain the same IP. Choose a Rotating Session when different IPs are preferred.

**Concurrency**

For applications sending multiple requests simultaneously, check the proxy service's supported concurrent connections and overall connection stability.

**Response Speed**

Proxy performance is affected by factors such as network distance, proxy server response time, and target server processing time. Measuring actual request performance can provide more useful information than relying on Ping alone.

## 9. Common Proxy Configuration Issues

### Proxy Connection Failed

If you encounter a `ProxyError`, check the following:

- Whether the proxy host and port are correct
- Whether the username and password are correct
- Whether the proxy is still active
- Whether your network can connect to the proxy server
- Whether the proxy type matches the configured protocol

### Request Timeout

You can set a timeout for Requests:

```text
response = requests.get(
    "https://example.com",
    proxies=proxies,
    timeout=10
)
```

If the proxy responds slowly, you can adjust the timeout value while also checking the proxy's response time and connection stability.

### HTTPS Request Failed

When an HTTPS request fails, check the proxy protocol, port, and whether the proxy service supports HTTPS requests. The issue is not necessarily caused by the target URL using HTTPS.

## Conclusion

Configuring a proxy with Python Requests is straightforward. The main step is to specify the proxy server through the `proxies` parameter.

For multiple requests, `Session` can simplify proxy management. When different IPs are required, Rotating Residential Proxies can be considered, while Sticky Sessions are useful when consecutive requests need to maintain the same IP.

By considering proxy protocol, IP type, Session behavior, concurrency, and response speed, developers can select a proxy configuration that better fits their Requests-based applications.
