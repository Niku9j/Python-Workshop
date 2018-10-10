def palindrome(string):
    '''
    Objective: To determine whether the given string is a palindrome.
    Input Parameter: string
    Return Value: True if string is a palindrome,  False otherwise
    '''
    '''
    Approach:
        For each position i in string, check if elements at i and
        len(string)-(i-1) th locations are same. If this holds true for all i
        in range [1, len(string)/2] return True else False.
    '''
    n = len(string)
    if n == 0: #null string
        return True
    else:
        j = n-1 #index of rightmost character
        for i in range(n//2+1):
            if string[i] != string[j]:
                return False #character mismatch
            j -= 1
        return True

def main():
    '''
    Objective: To check whether the given string is a palindrome or not
    Input parameter: None
    Return alue: None
    '''
    '''
    Approach:  To use function palindrome
    '''
    myString = input('Enter a string to check:')
    if palindrome(myString):
        print('String "%s" is a Palindrome' %(myString))
    else:
        print('String "%s" is not a Palindrome' %(myString))

if __name__ == '__main__':
    main()
