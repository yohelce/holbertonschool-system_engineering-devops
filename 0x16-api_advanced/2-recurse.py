#!/usr/bin/python3
"""Module for Recurse"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': "My-User-Agent"}
    params = {'after': after, 'count': count}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list