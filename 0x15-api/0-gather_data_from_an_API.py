#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1]))
    name = user.json().get('name')

    json_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in json_todo:
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with task({}/{}):'
          .format(name, completed, totalTasks))

    [print("\t {}".format(title_task)) for title_task in task.get('title')]
