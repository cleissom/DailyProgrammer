import re

filename = '../input.txt'

with open(filename) as file:
    line = file.read()

array = re.findall(r'[0-9] [0-9] [0-9]', line)
print(array)
