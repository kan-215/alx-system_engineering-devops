#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response was successful
        if response.status_code != 200:
            return 0

        # Parse JSON response
        data = response.json()
        # Extract the number of subscribers
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers

    except Exception:
        # Return 0 in case of any exception (e.g., network issues)
        return 0
