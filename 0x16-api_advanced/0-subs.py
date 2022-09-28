#!/usr/bin/python3
"""Module for number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if (response.status_code == 200):
        return response.json().get("data").get("subscribers")
    else:
        return 0
