"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod,)
while True:
    input_string = input(">  ")
    if len(input_string)>4:
        calc_input = input_string.split(' ')
        operator = calc_input[0]
        num1 = calc_input[1]
        num2 = calc_input[2]
        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            print(add(num1,num2))

        elif operator == "-":  
            print(subtract(num1, num2))
            
    elif input_string == "q":
        break
    else:
        print("please enter an operator and 2 numbers")

# Replace this with your code
