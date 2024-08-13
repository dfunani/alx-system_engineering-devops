#!/usr/bin/python3
"""Reddit API - Subscribers"""
import requests

BASE_URL = "https://www.reddit.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 Linux 6.0 Edg/127.0.0.0"
}

def number_of_subscribers(subreddit):
    """Retrieves the Subscribers.

    Args:
        subreddit (str): sub-reddit aka reddit group.
    """
    endpoint = f"r/{subreddit}/about.json"
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS, allow_redirects=False)
    if response.ok:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
