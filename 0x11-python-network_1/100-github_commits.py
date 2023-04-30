#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    username = argv[2]
    repos = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(username, repos)
    response = get(url)
    try:
        objs = response.json()
        for i, obj in enumerate(objs):
            print('{}: {}'.format(obj.get('sha'), obj.get('commit').get('author').get('name')))
            if i == 9:
                break
    except ValueError:
        pass
