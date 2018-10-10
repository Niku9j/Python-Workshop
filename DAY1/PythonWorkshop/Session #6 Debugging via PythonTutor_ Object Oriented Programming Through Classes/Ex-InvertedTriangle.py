def invertedRightTriangle(nRows):
    '''
    Objective: To print right triangle
    Input Parameter: nRows – integer value
    Return Value: None
    '''
    for i in range(nRows, 0):
        print('*' * i)

def main():
    '''
    Objective: To print right triangle
    Input Parameter: None
    Return Value: None
    '''
    nRows = int(input('Enter no. of rows: '))
    invertedRightTriangle(nRows)
        
if __name__=='__main__':
    main()
