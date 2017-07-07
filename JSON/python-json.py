#!python
# -*-coding:utf-8 -*-

import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json_str = json.dumps(data)
print json_str

print json.dumps({'a': 'Runable', 'b': 7}, sort_keys = True, indent = 10, separators = (',', ':'))

jsonData = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
text = json.loads(jsonData)
print text

