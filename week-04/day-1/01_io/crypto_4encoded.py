# Create a method that decrypts texts/encoded_zen_lines.txt

def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    f.close()
    new_list = []
    for row in text:
        new_row = ''
        for char in range(len(row)-1):
            new_char = ord(row[char])
            if new_char != 32:
                new_row += chr(new_char-1)
            else:
                new_row += ' '
        new_list.append(new_row + '\n')
    result = ''.join(new_list)
    return result

decrypt('texts/encoded_zen_lines.txt')
