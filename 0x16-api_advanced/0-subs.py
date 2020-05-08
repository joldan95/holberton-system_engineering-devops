#!/usr/bin/python3
"""
Shows the number of suscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url,
                            headers={'User-agent': 'Mozilla/5.0'},
                            allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
