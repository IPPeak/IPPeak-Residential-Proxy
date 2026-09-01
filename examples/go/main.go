package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
)

const (
	proxyHost     = "HOST"
	proxyPort     = "PORT"
	proxyUsername = "USERNAME"
	proxyPassword = "PASSWORD"
)

func main() {
	proxyURL := &url.URL{
		Scheme: "http",
		Host:   proxyHost + ":" + proxyPort,
	}

	proxyURL.User = url.UserPassword(
		proxyUsername,
		proxyPassword,
	)

	client := &http.Client{
		Transport: &http.Transport{
			Proxy: http.ProxyURL(proxyURL),
		},
	}

	targetURL := "https://httpbin.org/ip"

	resp, err := client.Get(targetURL)
	if err != nil {
		fmt.Println("Request failed:", err)
		return
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Failed to read response:", err)
		return
	}

	fmt.Println("Request successful!")
	fmt.Println("Status:", resp.Status)
	fmt.Println("IP response:")
	fmt.Println(string(body))
}
