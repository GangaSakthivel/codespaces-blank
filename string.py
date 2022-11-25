my_string = " The quick brown fox jumps over the lazy dog  "
print("Upper case:", my_string.upper())
print("String after removed white spaces:", my_string.replace(" ", ""))
count: int = 0
for i in my_string:
    if i == 'o':
        count = count + 1
print("The letter 'o' occurance is:", str(count))

def reversed_str(myy_string):
    return myy_string[::-1]
print("Letters backwards in given string:", reversed_str(my_string))
