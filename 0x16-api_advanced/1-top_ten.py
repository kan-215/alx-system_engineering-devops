#!/usr/bin/python3
"""Function to query and print the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        None: Prints the titles of the first 10 hot posts or None if invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}

    try:
        # Make the request to Reddit API
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        
        # If subreddit is invalid, print None
        if response.status_code != 200:
            print(None)
            return
        
        # Parse the JSON response
        data = response.json().get("data")
        
        # Extract titles from the hot articles
        hot_articles = data.get("children", [])
        for article in hot_articles:
            title = article.get("data").get("title")
            print(title)

    except (requests.RequestException, ValueError, AttributeError):
        # Print None for any error in the request or parsing the JSON
        print(None)
