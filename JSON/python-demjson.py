#!python
# -*-coding:utf-8 -*-

import demjson

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json_str = demjson.encode(data)
print json_str

jsonData = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
text = demjson.decode(jsonData)
print text
