# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def separate(characters):
    if len(characters) == 1:
        return characters
    else:
        return characters[0] + '*' + separate(characters[1:])



print(separate('qwerty'))
