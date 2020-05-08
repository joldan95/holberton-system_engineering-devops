#!/usr/bin/python3
"""
Top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    response = requests.get(url,
                            headers={'User-agent': 'Mozilla/5.0'},
                            allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
