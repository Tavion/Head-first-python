import os
os.getcwd()
os.chdir('/Users/tavion/百度云同步盘/sync/sync/Python files/chapter3')
os.getcwd()
data=open('sketch.txt')
print(data.readline(),end='')


data.seek(0)
"""For Python files, tell() can also be used"""

for each_item in data:
    print(each_item,end='')

