try:
    with open('missing.txt', 'w') as data:
        print('missing', file=data)
except IOError as err:
    print('File error:' + str(err))
