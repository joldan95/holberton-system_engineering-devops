#!/usr/bin/python3
"""
Export all users data to a json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    status_code = 200
    user_id = 1
    user_todos = dict()
    while status_code == 200:
        url = 'https://jsonplaceholder.typicode.com/users/{}'
        user = requests.get(url.format(user_id))
        if user.status_code == 200:
            todos = requests.get(url.format(user_id) + '/todos').json()
            for todo in todos:
                todo.pop('userId')
                todo.pop('id')
                todo['task'] = todo['title']
                todo.pop('title')
                todo['username'] = user.json()['username']
            user_todos[user_id] = todos
        user_id += 1
        status_code = user.status_code
    with open("todo_all_employees.json", "w") as user_file:
        json.dump(user_todos, user_file)
