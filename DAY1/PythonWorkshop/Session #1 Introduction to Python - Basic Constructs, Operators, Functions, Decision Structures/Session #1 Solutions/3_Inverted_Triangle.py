def invertedRightTriangle(rows):
    '''
    Objective: To print an inverted triangle comprising of asterisks
    Input Parameter: rows - numeric
    Return Value: None
    '''
    start, end, step = rows, 0, -1
    for i in range(start, end, step):
        print('*' * i)
    
def main():
    '''
    Objective: To compute factorial of a number provided as an input
    Input Parameter: None
    Return Value: None
    '''
    rows = int(input('Enter the number: '))
    invertedRightTriangle(rows)

if __name__ == '__main__':
    main()

