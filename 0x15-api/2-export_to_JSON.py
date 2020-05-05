#!/usr/bin/python3
"""
Export user data to a CSV format
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'
    user_id = sys.argv[1]
    user = requests.get(url.format(user_id))
    if user.status_code == 200:
        todos = requests.get(url.format(user_id) + '/todos').json()
        for todo in todos:
            todo.pop('userId')
            todo.pop('id')
            todo['username'] = user.json()['username']
        user_todos = {"{}".format(user_id): todos}
        with open("{}.json".format(user_id), "w") as user_file:
            json.dump(user_todos, user_file)
