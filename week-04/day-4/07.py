# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def change(characters):

    if len(characters) == 0:
        return ''

    elif characters[0] == 'x':
        return 'y' + change(characters[1:])

    else:
        return characters[0] + change(characters[1:])

print(change('xxxdxxxdxxxgxxxxhxx'))
