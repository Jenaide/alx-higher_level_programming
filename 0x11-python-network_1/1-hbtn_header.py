#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urloprn(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
