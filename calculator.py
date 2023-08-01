print("************************CALCULATOR************************")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def calculator(operator):
    
    if operator == '+':
        sum = a+b
        print(f'{a} + {b} = {sum}')
        
    elif operator == '-':
        diff = a-b
        print(f'{a} - {b} = {diff}')
        
    elif operator == 'x':
        product = a*b
        print(f'{a} x {b} = {product}')
        
    elif operator == '/':
        quotient = a/b
        print(f'{a} / {b} = {quotient}')
        
    elif operator == '%':
        remainder = a%b
        print(f'{a} % {b} = {remainder}')
        
    elif operator == '^':
        exp = a**b
        print(f'{a} ^ {b} = {exp}')
        
    else:
        print("Invalid Operator")
        
calculator(operator=input("Select the operator: "))

