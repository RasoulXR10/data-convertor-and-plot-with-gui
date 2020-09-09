import numpy
import re

# txt = open("sample.txt", "r")

with open('sample.txt') as f:
    mylist = [line.rstrip('\n') for line in f]
res = []
for element in mylist[1:]:
    res.append(element)
result = [tuple(map(int, sub.split())) for sub in res]
print(result)
