#!/usr/bin/python3
"""
Returns info about a user TODO list
The user related to teh id passed by parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}' 
    user_id = sys.argv[1]
    user = requests.get(url.format(user_id))
    if user.status_code == 200:
        todo_list = requests.get(url.format(user_id) + '/todos').json()
        complete = list(filter(lambda todo: todo['completed'] == True, todo_list))
        complete = list(task['title'] for task in complete)
        print("Employee {} is done with tasks({:d}/{:d}):".format(user.json()['name'],
                                                                  len(complete),
                                                                  len(todo_list)),
              *complete, sep='\n\t ')
