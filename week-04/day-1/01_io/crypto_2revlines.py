# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    f.close()
    result = ''
    for row in text:
        row_wo_enter = row[0:-1]
        result = result + row_wo_enter[::-1] + '\n'
    return result

decrypt('texts/reversed_zen_lines.txt')
