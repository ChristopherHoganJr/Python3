from logo_art import logo
from operations import Add, Subtract, Multiply, Divide

operations = {
    '+': Add, 
    '-': Subtract, 
    '*': Multiply, 
    '/': Divide
    }

def calculator():
    print(logo)
    num1 = float(input('What\'s the first number?: '))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation from the line above: ')
        num2 = float(input('What\'s the next number?: '))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f'Type \'y\' to continue with {answer}, or type \'n\' to start a new calculation: ') == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()