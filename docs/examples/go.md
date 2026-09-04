---
layout: default
title: Go Examples
---

# Go Examples

This guide explains how to integrate IPPeak proxy services with Go applications.
The example demonstrates how to configure HTTP proxy connections using Go's standard HTTP client.

## Requirements

Before running the example, make sure you have:

- Go 1.20+
- An active IPPeak proxy account

Check your Go version:

```bash
go version
```

## Proxy Configuration

IPPeak proxy uses standard authentication format:

```
http://username:password@host:port
```

Example:

```
http://user123:pass123@proxy.example.com:8080
```

Replace:

- `username`
- `password`
- `host`
- `port`

## HTTP Proxy Example

Source file:

`examples/go/main.go`

The example uses Go's built-in HTTP client with proxy configuration.

Example:

```go
package main

import (
    "fmt"
    "net/http"
    "net/url"
)

func main() {
    proxyURL, err := url.Parse(
        "http://username:password@host:port",
    )
    if err != nil {
        panic(err)
    }

    client := &http.Client{
        Transport: &http.Transport{
            Proxy: http.ProxyURL(proxyURL),
        },
    }

    response, err := client.Get(
        "https://example.com",
    )
    if err != nil {
        panic(err)
    }

    fmt.Println(response.Status)
}
```

## Run Example

Enter the example directory:

```bash
cd examples/go
```

Run:

```bash
go run main.go
```

## Use Cases

Go proxy integration is suitable for:

### Backend Applications
Add proxy support to server-side applications.

### Automation Tools
Build scalable network workflows.

### Data Applications
Process requests with flexible proxy connections.

## Troubleshooting

### Authentication Error
Check:

- Username
- Password
- Proxy endpoint

### Connection Timeout
Check:

- Proxy availability
- Network connection
- Request configuration

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
