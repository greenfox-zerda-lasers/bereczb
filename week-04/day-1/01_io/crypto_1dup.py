# Create a method that decrypts the texts/duplicated_chars.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    f.close()
    result = ''
    for row in text:
        line = ''
        for char in range(0, len(row), 2):
            line = line + row[char]
        result += line
    return result

decrypt('texts/duplicated_chars.txt')
