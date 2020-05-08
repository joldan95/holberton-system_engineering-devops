#!/usr/bin/python3
"""
List the titles of all hot articles of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    url += "?after={}".format(after) if after != "" else ""
    response = requests.get(url,
                            headers={'User-agent': 'Mozilla/5.0'},
                            allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        next_page = response.json()['data']['after']
        if next_page is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, next_page)
    else:
        return None
