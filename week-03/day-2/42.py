filename = 'alma.txt'
# write a function that reads a file and prints how many
# lines and characters in it

def readfile(file_to_read):
    f = open(file_to_read)
    text = f.read()
    f.close()
    result1 = 0
    result2 = 0
    for i in range(len(text)):
        if text[i] == '\n':
            result1 += 1
        else:
            result2 += 1
    return result1, result2

lines, strings = (readfile(filename))

print('lines: ', lines)
print('characters: ', strings)
