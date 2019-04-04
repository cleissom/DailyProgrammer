import re

filename = '../input.txt'

with open(filename) as file:
    lines = file.readlines()

intarray = [list(line.strip('[] \n\r').split()) for line in lines]

size = len(intarray[1])
middle = int(size/2)

availible = int("".join(intarray[0]))

processes = [(i, int("".join(intarray[i][0:middle])), int("".join(intarray[i][middle:]))) for i in range(1, len(intarray))]
print(processes)