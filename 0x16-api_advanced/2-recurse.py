#!/usr/bin/python3
"""Function to recursively query hot articles on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"after": after}

    try:
        # Make the request to Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # If subreddit is invalid, return None
        if response.status_code != 200:
            return None
        
        # Parse the JSON response
        data = response.json().get("data")
        after = data.get("after")
        
        # Extract titles from the hot articles
        hot_articles = data.get("children", [])
        for article in hot_articles:
            hot_list.append(article.get("data").get("title"))
        
        # Base case: If there is no more pagination, return the list
        if after is None:
            return hot_list
        
        # Recursive case: Call the function again with the next page
        return recurse(subreddit, hot_list, after)
    
    except (requests.RequestException, ValueError, AttributeError):
        # Return None for any error in the request or parsing the JSON
        return None
