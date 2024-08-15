#!/usr/bin/python3

import requests


def top_ten(subreddit):
    # REDDIT api that gets hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # agent user that helps avoid merrors
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Makes a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful with status code 200
    if response.status_code == 200:
        # get titles of hot posts from the JSON response
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        # Print None if the request fails
        print(None)


subreddit = "python"
top_ten(subreddit)
