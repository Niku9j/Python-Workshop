def removeDuplicates(lst1):
    '''
    Objective: To return another list without any duplicates from the input list
    Input Parameter: lst1- list with duplicate elements
    Return Value: lst2 - list without duplicate elements
    '''
    lst2 = []
    for el in lst1:
        if el not in lst2:
            #if the element el is not already in lst2, concatenate el with lst2
            lst2.append(el)
    return lst2

def main():
    '''
    Objective: To remove duplicate from a list
    Input parameter: None
    Output: None
    '''
    myList = eval(input('Enter the list='))
    result = removeDuplicates(myList)
    print('List with no duplicates::' ,result)

if __name__ == '__main__':
    main()
