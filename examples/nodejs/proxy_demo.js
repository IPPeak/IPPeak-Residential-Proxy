const axios = require("axios");
const { HttpsProxyAgent } = require("https-proxy-agent");

const PROXY_HOST = "HOST";
const PROXY_PORT = "PORT";
const PROXY_USERNAME = "USERNAME";
const PROXY_PASSWORD = "PASSWORD";

const proxyUrl =
    `http://${encodeURIComponent(PROXY_USERNAME)}:` +
    `${encodeURIComponent(PROXY_PASSWORD)}@` +
    `${PROXY_HOST}:${PROXY_PORT}`;

const agent = new HttpsProxyAgent(proxyUrl);

const targetUrl = "https://httpbin.org/ip";

async function main() {
    try {
        const response = await axios.get(targetUrl, {
            httpsAgent: agent,
            proxy: false,
            timeout: 30000
        });

        console.log("Request successful!");
        console.log("IP response:");
        console.log(response.data);
    } catch (error) {
        console.error("Request failed:", error.message);
    }
}

main();
