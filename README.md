# HTTP Method Scanner

A small Python tool that checks which HTTP methods a server accepts for a given URL.

It sends a request with each common method (GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE) and prints the status code and response size for each one. This helps spot misconfigured endpoints, for example a PUT or DELETE that a server shouldn't allow.

## Install

```
pip install -r requirements.txt
```

## Usage

Pass the URL as an argument:

```
python http_method_scanner.py https://example.com
```

Or run it and enter the URL when prompted:

```
python http_method_scanner.py
Enter the URL: https://example.com
```

Example output:

```
https://example.com
GET: 200 - 1256
POST: 405 - 0
PUT: 405 - 0
DELETE: 405 - 0
HEAD: 200 - 0
OPTIONS: 204 - 0
PATCH: 405 - 0
TRACE: 405 - 0
```

Optional timeout flag:

```
python http_method_scanner.py https://example.com --timeout 5
```

## Note

Only use this on systems you own or have explicit permission to test.

TLS certificate verification is skipped (like curl -k) so the tool also works against lab targets with self-signed certificates.
