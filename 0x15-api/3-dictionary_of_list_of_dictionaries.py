#!/usr/bin/python3
""" This script exports data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    filename = 'todo_all_employees.json'
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    json_users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    json_todos = todos.json()
    data = {}

    for user in json_users:
        data_user = []
        for task in json_todos:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                data_user.append(task_dict)
        data[user.get('id')] = data_user

with open(filename, mode='w') as f:
    json.dump(data, f)
