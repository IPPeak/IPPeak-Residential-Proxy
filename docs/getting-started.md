---
layout: default
title: Getting Started
permalink: /getting-started/
---

# Getting Started

This guide explains how to get started with the proxy service.

## 1. Choose a Proxy Type

Select a proxy type based on your use case.

### Residential Proxies

Residential proxies use IP addresses associated with real residential networks.

They are suitable for applications that require a residential IP environment and flexible IP rotation.

### Static Residential Proxies

Static residential proxies provide a persistent IP address for scenarios that require a stable connection.

### Unlimited Residential Proxies

Unlimited residential proxies are designed for workloads that require high-volume traffic without traditional traffic-based limits.

## 2. Get Your Proxy Credentials

After selecting a proxy product, obtain the required connection information:

- Proxy host
- Proxy port
- Username
- Password

Keep your credentials secure and do not publish them in public repositories.

## 3. Configure Your Connection

A typical HTTP proxy configuration looks like:

```text
Host: proxy.example.com
Port: 10000
Username: your_username
Password: your_password
```

Replace the example values with your actual proxy credentials.

## 4. Test Your Connection

Example command:

```bash
curl -x http://username:password@proxy.example.com:10000 https://example.com
```

If the request succeeds, the proxy connection is working correctly.

## 5. Session Strategy

### Rotating Session

The proxy IP changes automatically according to the rotation settings.

Recommended for applications requiring multiple IP addresses.

### Sticky Session

The same IP address is maintained during a session period.

Recommended for applications requiring connection stability.

## Next Steps

Continue reading:

```text
-[Proxy Types]({{ '/proxy-types/' | relative_url }})
-[API Reference]({{ '/api/' | relative_url }})
-[Python Examples]({{ '/examples/python/' | relative_url }})
-[Go Examples]({{ '/examples/go/' | relative_url }})
-[Node.js Examples]({{ '/examples/nodejs/' | relative_url }})
```
