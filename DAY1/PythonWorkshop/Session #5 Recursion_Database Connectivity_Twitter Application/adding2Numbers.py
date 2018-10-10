def add(num1, num2):
    '''
    Objective: To add two numbers recursively
    Input Parameters: num1, num2 - numeric
    Return Value: sum - numeric
    '''
    if num2 == 0:
        return num1
    else:
        return add(num1, num2 - 1) + 1

def main():
    '''
    Objective: To add two numbers recursively
    Input Parameter: None
    Return Value: None
    '''
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    result = add(num1, num2)
    print('Result: ', result)

if __name__=='__main__':
    main()
