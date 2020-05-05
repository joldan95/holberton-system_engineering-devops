#!/usr/bin/python3
"""
Export user data to a CSV format
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'
    user_id = sys.argv[1]
    user = requests.get(url.format(user_id))
    if user.status_code == 200:
        todos = requests.get(url.format(user_id) + '/todos').json()
        with open("{}.csv".format(user_id), "w") as user_file:
            for task in todos:
                s = "\"{}\",\"{}\",\"{}\",\"{}\""
                s = s.format(user_id,
                             user.json()["username"],
                             task["completed"],
                             task["title"])
                print(s, file=user_file)
