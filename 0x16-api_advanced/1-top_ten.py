#!/usr/bin/python3
"""Module for Top ten"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if (response.status_code == 200):
        top_ten = response.json().get("data").get("children")
        for element in top_ten[:10]:
            print(element.get("data").get("title"))
    else:
        print("None")
