from sanitize import *


def get_coach_data(filename):
    try:
            with open(filename) as f:
                data = f.readline()
            return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

clean_james = sorted([sanitize(each_t) for each_t in james])
clean_julie = sorted([sanitize(each_t) for each_t in julie])
clean_mikey = sorted([sanitize(each_t) for each_t in mikey])
clean_sarah = sorted([sanitize(each_t) for each_t in sarah])

unique_james = sorted(list(set(clean_james)))
unique_julie = sorted(list(set(clean_julie)))
unique_mikey = sorted(list(set(clean_mikey)))
unique_sarah = sorted(list(set(clean_sarah)))

print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])
