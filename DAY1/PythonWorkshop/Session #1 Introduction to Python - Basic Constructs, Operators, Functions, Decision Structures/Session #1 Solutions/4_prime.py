def isPrime(n):
    '''
    Objective: To check if a number is prime or not
    Input Parameter: n - numeric value
    Return Value: message – boolean value
    '''
    '''
    Approach: Check to find out if there is any factor of number n or not.
    All the numbers in the range [3, root(n)] are checked for factor test.
    '''
    if n == 1: # 1 is not prime
        return False
    limit = int (round(n ** 0.5))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True

def main():
    '''
    Objective: To check if the number entered by the user is a
    prime number
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter number: '))
    result = isPrime(n)
    if result == True:
        print(n, 'is a prime number')
    else:
        print(n, 'is not a prime number')

if __name__ == '__main__':
    main()

