from sanitize import *

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

clean_james = sorted([sanitize(each_t) for each_t in james])
clean_julie = sorted([sanitize(each_t) for each_t in julie])
clean_mikey = sorted([sanitize(each_t) for each_t in mikey])
clean_sarah = sorted([sanitize(each_t) for each_t in sarah])

unique_james = []

for each_t in clean_james:
    if each_t not in unique_james:
        unique_james.append(each_t)

print(unique_james[0:3])
