def findFactors(num):
    '''
    Objective: To find the list of factors of a given number.
    Input Parameter: num - numeric
    Return Value: total - numeric
    '''
    '''
    Approach: Determine factors of n in the range [1,n].

    '''
    factors = ()
    for i in range(1, num + 1):
        if num % i == 0:
            factors = factors + (i,)
    return factors


def main():
    '''
    Objective: To find and print list of factors of first few numbers.
    Input Parameter: None
    Return Value: None
    '''
    limit = int(input('Enter the upper limit:'))
    for i in range(1, limit + 1):
        print('Number:', i, 'List of factors=', findFactors(i))

if __name__ == '__main__':
    main()

