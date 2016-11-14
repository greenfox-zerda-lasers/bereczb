string1 = 'alma'
string2 = 'Lam a'

def anagramm(string1, string2):
    if isinstance(string1, str) == False or isinstance(string2, str) == False:
        raise TypeError
    return dictionary(string1) == dictionary(string2)

def count_letters(string):
    if isinstance(string1, str) == False or isinstance(string2, str) == False:
        raise TypeError
    string = string.lower()
    dict_of_string = {}
    for i in string:
        if i != ' ' and i.isalpha():
            dict_of_string[i] = string.count(i)
    return dict_of_string

def dictionary(string):
    string = string.lower()
    dict_of_string = {}
    for i in string:
        if i != ' ':
            dict_of_string[i] = string.count(i)
    return dict_of_string

# print(count_letters(string1))
# print(count_letters(string2))
#
# print(anagramm(string1, string2))
#
anagramm(string1, string2)
