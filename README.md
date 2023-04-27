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

## Troubleshooting
Typically, there could be a problem with connecting to the SOCKS5 proxy server at localhost:9051, for ex. the "connection is being refused", which means that the proxy server may not be running, or it may be running on a different port. To troubleshoot such network issues, you can try the following:

see which ports are being used by Tor
```bash
sudo netstat -tlnp | grep tor
```

or
```bash
cat /etc/tor/torrc | grep ControlPort
```

Verify that the Tor service is running
```bash
sudo systemctl status tor
```

Check/add your user to the debian-tor
```bash
sudo adduser <your-username> debian-tor
```

Check that the Tor proxy settings are correct. By default, the Tor control port is not enabled. To enable it, you need to add/uncomment the following lines to your torrc file and restart the Tor service
```bash
ControlPort 9051
CookieAuthentication 1
```

If the Tor service is running and the proxy settings are correct, try restarting the Tor service
```bash
sudo systemctl restart tor
```

If none of the above steps work, try connecting to the Tor network using a different Tor client
