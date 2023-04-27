# onionScraper

onionScraper is a Python script for .onion web site scraping.

## Installation

Assuming that you have Python and pip already installed, you can then install the necessary dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

```python
python3 onionScraper.py
```

## Connection troubleshooting
Typically, there could be a problem with connecting to the SOCKS5 proxy server at localhost:9051, for ex. the "connection is being refused", which means that the proxy server may not be running, or it may be running on a different port. To troubleshoot such network issues, you can try the following:
- netstat command to see which ports are being used by Tor:
```bash
sudo netstat -tlnp | grep tor
```
- Also the following tp check the Tor port:
```bash
cat /etc/tor/torrc | grep ControlPort
```
- Verify that the Tor service is running:
```bash
sudo systemctl status tor
```
- Check/add your user to the debian-tor
```bash
sudo adduser <your-username> debian-tor
```
- Control port is not enabled: By default, the Tor control port is not enabled. To enable it, you need to add the following lines to your torrc file:
```bash
ControlPort 9051
CookieAuthentication 1
```
You can find the torrc file in the Tor installation directory (e.g. /etc/tor/torrc on Linux). Once you have added these lines, restart the Tor service.
- Check that the Tor proxy settings are correct. Make sure that the proxy host is set to localhost and the port is set to 9050.
- If the Tor service is running and the proxy settings are correct, try restarting the Tor service:
```bash
sudo systemctl restart tor
```
- If none of the above steps work, try connecting to the Tor network using a different Tor client