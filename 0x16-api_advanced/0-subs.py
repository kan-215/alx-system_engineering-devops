#!/usr/bin/python3
"""
Contains the number_of_subscribers function that queries the Reddit API
to get the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response was successful (status code 200)
        if response.status_code != 200:
            return 0

        # Parse JSON response
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers

    except requests.RequestException:
        # Return 0 if there's any exception (e.g., network issues)
        return 0
