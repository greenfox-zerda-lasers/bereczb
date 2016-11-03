filename = 'alma.txt'
# create a function that prints the content of the
# file given in the input

def readfile(file_to_read):
    f = open(file_to_read)
    text = f.read()
    f.close()
    return text

print(readfile(filename))
