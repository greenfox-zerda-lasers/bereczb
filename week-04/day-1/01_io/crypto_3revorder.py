# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    f.close()
    result = ''
    text_new_order = text[::-1]
    for row in text_new_order:
        result = result + row
    return result

decrypt('texts/reversed_zen_order.txt')
