import sys

for line in sys.stdin:
    lower, upper, digit, space = 0, 0, 0, 0
    
    for char in line:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            if char != '\n':
                space += 1
                
    print(lower, upper, digit, space)