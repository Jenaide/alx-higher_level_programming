#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    reponse = get(url)
    info = repsonse.headers
    print(info.get('x-request-id'))
