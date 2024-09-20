# Definitions:
def validate_operation(operation):
    if operation not in [1, 2, 3, 4, 5, 6]:
        print('Invalid operation. Please choose from 1 to 6.')
        return False
    return True

def calculate(operation, num_1, num_2):
    if operation == 1:
        return num_1 + num_2
    elif operation == 2:
        return num_1 - num_2
    elif operation == 3:
        return num_1 * num_2
    elif operation == 4:
        if num_2 == 0:
            print('Error: Division by 0 is not allowed.')
            return None
        return num_1 / num_2
    elif operation == 5:
        return num_1 ** num_2
    else:
        return num_1 % num_2

# Main Program:
while True:
    print('1. Addition\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent\n6. Modulo')
    operation = input('Enter operation of choice (1-6): ')
    
    try:
        operation = int(operation)
    except ValueError:
        print('Invalid input. Please enter an integer.')
        continue

    if validate_operation(operation):
        print('Enter two numbers:')
        
        num_1 = input('First number: ')
        num_2 = input('Second number: ')

        try:
            num_1 = float(num_1)
            num_2 = float(num_2)
        except ValueError:
            print('Invalid input. Please enter numeric values for both numbers.')
            continue

        result = calculate(operation, num_1, num_2)
        if result is not None:
            print('Result =', result)
    
    continue_choice = input('Do you want to perform another calculation? (Yes/No): ')
    if continue_choice.lower() != 'yes':
        print('Goodbye!')
        break
