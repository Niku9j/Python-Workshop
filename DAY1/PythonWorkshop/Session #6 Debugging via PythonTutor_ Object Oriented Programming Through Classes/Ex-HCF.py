def findHCF(num1, num2):
    '''
    Objective: To find HCF of two numbers, num1 and num2.
    Input Parameters: num1, num2 - numeric values
    Return Value: HCF - numeric value
    '''
    if num1 < num2:
        minNum = num1
    else:
        minNum = num2
    for i in range(minNum,1,-1):
        if (num1 % i == 0) and (num2 % i == 0):
            HCF = i
    return HCF

def main():
    '''
    Objective: To take two numbers as an input and find their HCF
    Input Parameter: None
    Return Value: None
    '''
    num1 = int(input('Enter first number:: '))
    num2 = int(input('Enter second number:: '))
    print(findHCF(num1, num2))

if __name__=='__main__':
    main()
