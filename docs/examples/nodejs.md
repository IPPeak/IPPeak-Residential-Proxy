---
layout: default
title: Node.js Examples
---

# Node.js Examples

This guide explains how to integrate IPPeak proxy services with Node.js applications.
The example demonstrates how to configure proxy connections using JavaScript and common HTTP request libraries.

## Requirements

Before running the example, make sure you have:

- Node.js 18+
- npm package manager
- An active IPPeak proxy account

Check your Node.js version:

```bash
node -v
```

Check npm:

```bash
npm -v
```

## Install Dependencies

Navigate to the Node.js example directory:

```bash
cd examples/nodejs
```

Install required packages:

```bash
npm install axios
```

## Proxy Configuration

IPPeak proxy uses standard authentication:

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

`examples/nodejs/proxy_demo.js`

The example uses Axios to send requests through an IPPeak proxy connection.

Example:

```js
const axios = require("axios");

const proxy = {
    host: "proxy.example.com",
    port: 8080,
    auth: {
        username: "username",
        password: "password"
    }
};

axios.get(
    "https://example.com",
    {
        proxy: proxy
    }
)
    .then(response => {
        console.log(response.status);
    })
    .catch(error => {
        console.error(error);
    });
```

## Run Example

Enter the example directory:

```bash
cd examples/nodejs
```

Run:

```bash
node proxy_demo.js
```

## Use Cases

Node.js proxy integration is suitable for:

### Web Applications
Add proxy support to JavaScript applications.

### Automation Scripts
Build flexible automation workflows.

### Data Applications
Send requests through different proxy environments.

## Troubleshooting

### Proxy Authentication Failed
Check:

- Username
- Password
- Proxy address
- Proxy port

### Request Failed
Check:

- Network connection
- Proxy availability
- Request timeout settings

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
