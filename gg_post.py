#!/usr/bin/env python3
# coding=utf-8

import os
import sys
import json
import requests

from settings import (
    url,
    username,
    password,
)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('请使用./gg_post.py filename的方式来调用脚本')
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise Exception('{}文件不存在'.format(filename))

    data = {
        'username': username,
        'password': password,
    }
    files = {
        'graph': open(filename, 'rb'),
    }
    response = requests.post(url, data=data, files=files)
    print(json.loads(response.content))