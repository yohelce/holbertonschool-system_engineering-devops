#!/usr/bin/python3
""" Exports data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId))
    username = user.json().get("username")
    json_todo = todo.json()

    with open("{}.json".format(userId), "w", newline="") as jsonfile:
        json.dump({userId: [{
            "task": a.get("title"),
            "completed": a.get("completed"),
            "username": username}
            for a in json_todo]}, jsonfile)
