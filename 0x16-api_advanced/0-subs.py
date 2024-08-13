#!/usr/bin/python3
"""Reddit API - Subscribers"""
from requests import get

BASE_URL = "https://www.reddit.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"
}

def number_of_subscribers(subreddit):
    """Retrieves the Subscribers.

    Args:
        subreddit (str): sub-reddit aka reddit group.
    """
    endpoint = f"r/{subreddit}/about.json"
    url = f"{BASE_URL}{endpoint}"
    print(url)
    return url
    response = get(url, headers=HEADERS, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get("data").get("subscribers")
