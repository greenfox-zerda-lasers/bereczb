# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def change(characters):

    if len(characters) == 0:
        return ''

    elif characters[0] == 'x':
        return change(characters[1:])

    else:
        return characters[0] + change(characters[1:])

print(change('xxxdxxxdxxxgxxxxhxx'))
