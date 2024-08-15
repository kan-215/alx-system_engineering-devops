#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        # Make the request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the subreddit does not exist, return 0
        if response.status_code != 200:
            return 0

        # Parse the JSON response
        results = response.json().get("data")

        # Return the number of subscribers, or 0 if not found
        return results.get("subscribers", 0)

    except (requests.RequestException, ValueError, AttributeError):
        # Return 0 for any error in the request or parsing the JSON
        return 0
