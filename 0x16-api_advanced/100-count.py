#!/usr/bin/python3
"""Function to recursively query and count keywords in Reddit hot articles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries Reddit API, counts keywords in hot article titles,
    and prints the sorted count.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the titles.
        after (str): The pagination token for the next page of results.
        counts (dict): A dictionary to store the counts of the keywords.

    Returns:
        None: Prints the sorted counts.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"after": after}

    try:
        # Make the request to Reddit API
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        # If subreddit is invalid, return None (print nothing)
        if response.status_code != 200:
            return

        # Parse the JSON response
        data = response.json().get("data")
        after = data.get("after")

        # Extract titles from the hot articles
        hot_articles = data.get("children", [])
        for article in hot_articles:
            title = article.get("data").get("title").lower().split()

            # Count the keywords in the title
            for word in title:
                cleaned_word = word.strip('.,!?:;"\'-_()[]{}')
                if cleaned_word in counts:
                    counts[cleaned_word] += 1

        # Base case: If there is no more pagination, print the sorted counts
        if after is None:
            # Sort by count (descending) & by word (ascending) in case of ties
            sorted_counts = sorted(
                [(word, count) for word, count in counts.items() if count > 0],
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

        # Recursive case: Call the function again with the next page
        return count_words(subreddit, word_list, after, counts)

    except (requests.RequestException, ValueError, AttributeError):
        # Handle any error in the request or parsing the JSON
        return
