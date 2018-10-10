def sumEle(list1):
    '''
    Objective: To recursively find sum of elements
    of list
    Input Parameters: lst1 - list
    Return Value: numeric
    '''
    if list1 == []:
        return 0
    else:
        return list1[0] + sumEle(list1[1:])

def main():
    '''
    Objective: To recursively find sum of elements
    of list entered by user
    Input Parameter: None
    Return Value: None
    '''
    lst1 = eval(input('Enter the list: '))
    result = sumEle(lst1)
    print('Sum of elements of a List: ', result)

if __name__=='__main__':
    main()
