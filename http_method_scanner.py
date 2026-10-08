import argparse

import requests
from requests.exceptions import RequestException

# Suppress SSL warnings, since we skip certificate verification (like curl -k)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

METHODS = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH", "TRACE"]


def scan(url, timeout=10):
    print(url)
    for method in METHODS:
        try:
            response = requests.request(
                method,
                url,
                verify=False,   # skip TLS verification, like curl -k
                timeout=timeout,
                allow_redirects=False,
            )
            size = len(response.content)
            print(f"{method}: {response.status_code} - {size}")
        except RequestException as e:
            print(f"{method}: ERROR - {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Check which HTTP methods a server accepts for a given URL."
    )
    parser.add_argument("url", nargs="?", help="Target URL (e.g. https://example.com)")
    parser.add_argument(
        "-t", "--timeout", type=int, default=10, help="Request timeout in seconds (default: 10)"
    )
    args = parser.parse_args()

    url = args.url or input("Enter the URL: ").strip()
    scan(url, timeout=args.timeout)


if __name__ == "__main__":
    main()
