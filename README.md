# IPPeak Proxy Examples - Proxy Integration Guide

A developer-focused repository providing practical examples and documentation for integrating IPPeak proxy services into applications and development workflows.

## Features

- HTTP and SOCKS5 proxy support
- Residential, static, and unlimited proxy examples
- Rotating and sticky session configurations
- Python, Go, and Node.js integration examples
- Proxy authentication examples
- Practical proxy configuration examples

## Quick Start

### Installation

Clone the repository:

    git clone https://github.com/your-username/your-repository.git
    cd your-repository

Choose an example based on your preferred programming language:

    examples/
    ├── python/
    ├── go/
    └── nodejs/

Install the required dependencies according to the example you want to run.

### Basic Usage

Configure your proxy host, port, username, and password in the example configuration.

For HTTP or HTTPS connections, use an HTTP proxy configuration.

For applications that support SOCKS5, configure the proxy using the SOCKS5 protocol.

For rotating or sticky sessions, use the corresponding session configuration described in the documentation.

> Replace the example proxy credentials with your own IPPeak proxy credentials before running the examples.

## Documentation

- [Proxy Types](docs/proxy-types.md)
- [Authentication](docs/authentication.md)
- [API Reference](docs/api.md)

## Examples

### Python

- [Python HTTP Proxy](examples/python/)
- [Rotating Proxy](examples/python/rotating_proxy.py)
- [Sticky Session](examples/python/sticky_session.py)
- [SOCKS5 Proxy](examples/python/socks5_proxy.py)

### Go

- [Go Integration](examples/go/)
- [Proxy Example](examples/go/main.go)

### Node.js

- [Node.js Integration](examples/nodejs/)
- [Proxy Example](examples/nodejs/proxy_demo.js)

## FAQ

### What proxy protocols are supported?

The examples in this repository cover HTTP and SOCKS5 proxy connections.

### What is the difference between rotating and sticky sessions?

A rotating session periodically changes the proxy IP, while a sticky session keeps the same proxy IP for a defined period.

### Can I use these examples with my own proxy credentials?

Yes. Replace the example credentials with your own IPPeak proxy credentials before running the examples.

### Where can I find more information?

Check the documentation in the `docs` directory for proxy types, authentication, and API-related information.

## Contributing

Contributions are welcome.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting an issue or pull request.

For bug reports, use the available GitHub issue template. For feature suggestions, use the Feature Request template.

## License

This project is provided for educational and development purposes. Please review the repository license before using or redistributing the code.
