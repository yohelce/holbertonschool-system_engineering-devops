#!/usr/bin/python3
"""Python script that for a given employee ID returns all his todo list"""
import csv
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json().get("username")

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId))
    json_todo = todo.json()
    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, name, a.get("completed"), a.get("title")])
            for a in json_todo]
