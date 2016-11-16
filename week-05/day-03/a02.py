# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def number_of_lines(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return len(lines)

    except FileNotFoundError:
        return 0

print(number_of_lines('_01_.py'))
