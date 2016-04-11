def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def get_coach_data(filename):
    with open(filename) as f:
        data = f.readline()
        temple = data.strip().split(',')
    return {'name': temple.pop(0), 'DOB': temple.pop(0), 'Times': temple}


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james['name'] + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in james['Times']]))[0:3]))
# print(julie_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in julie]))[0:3]))
# print(mikey_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in mikey]))[0:3]))
# print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
