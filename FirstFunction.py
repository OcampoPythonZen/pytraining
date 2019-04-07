# Write a function that returns true if the brackets
#  in a given string are balanced. The function must handle parents (), 
#  square brackets [], and curly braces {}.
# String are iterables in python almost yet
import timeit

def my_brack_string(string_):
    opened = ['{','[','('] 
    closed = ['}',']',')']
    if not string_:
        return True
    count_opened = 0
    count_closed = 0
    for letter in string_:
        if letter in opened:
            count_opened =+ 1
        elif letter in closed:
            count_closed =+ 1
    if count_closed == count_opened:
        return True
    return False
    
# ------------------------------------------------------
def brack_string(string_):
    opened = ['{','[','('] 
    closed = ['}',']',')']
    openings_found = []
    for letter in string_:
        if letter in opened:
            openings_found.append(letter)
        elif letter in closed:
            if letter == ')' and openings_found[-1] != '(':
                return False
            elif letter == ']' and openings_found[-1] != '[':
                return False
            elif letter == '}' and openings_found[-1] != '{':
                return False
            elif letter == ')' and openings_found[-1] == '(':
                openings_found.pop()
            elif letter == ']' and openings_found[-1] == '[':
                openings_found.pop()
            elif letter == '}' and openings_found[-1] == '{':
                openings_found.pop()
    if not openings_found:
        return True
    return False

# ------------------------------------------------------
def brack_string_master(string_):
    characteres = {
        '{' : '}',
        '(' : ')',
        '[' : ']'
    }
    openings_found = []
    for letter in string_:
        if letter in characteres.keys():
            openings_found.append(letter)
        elif letter in characteres.values():
            if not openings_found:
                return False
            if letter == characteres[openings_found[-1]]:
                openings_found.pop()
            else:
                return False
    return not openings_found

if __name__ == "__main__":
    t1 = timeit.Timer("my_brack_string('({ (a + b) } + gt )')","from __main__ import my_brack_string")
    print('Ran my_brack_string function in :',t1.timeit(number=100000))
    
    t2 = timeit.Timer("brack_string('({ (a + b) } + gt )')","from __main__ import brack_string")
    print('Ran brack_string function in :',t2.timeit(number=100000))

    t3 = timeit.Timer("brack_string_master('({ (a + b) } + gt )')","from __main__ import brack_string_master")
    print('Ran brack_string_master function in :',t3.timeit(number=100000))

    print()

    print((my_brack_string('( a + b } + gt )')))
    print(brack_string('({ (a + b) } + gt )'))
    print(brack_string_master('({ (a + b) } + gt )'))