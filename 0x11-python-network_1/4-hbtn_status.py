#!/usr/bin/python3
"""
Created by jenaide Sibolie
"""
from requests import get


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    byte_code = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(type(byte_code), byte_code)
    print(string)
