import requests

def check_http(url):
    """
    Sends an HTTP GET request to the given URL and prints the result.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[OK] Service available : {url}")
        else:
            print(f"[ERREUR] Service unavailable ({response.status_code}): {url}")
    except requests.exceptions.RequestException as e:
        print(f"[ERREUR] Can't connect to {url} : {e}")

# URL list to test
urls = [
    "https://example.com/",
    "https://google.com/",
]

# URL testing
for url in urls:
    check_http(url) 