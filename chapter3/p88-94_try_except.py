data = open('sketch.txt')
for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said:', end='')
        print(line_spoken, end='')
    except:
        pass
data.close()
"""找不到问题的时候,增加额外代码解决问题的方式不比try/except更有效率"""
