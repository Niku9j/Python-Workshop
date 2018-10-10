def cumulativeList(lst1):
    '''
    Objective: To return another list whose ith element is the sum of all elements till ith element of lst1
    Input Parameter: lst1- list
    Return value: cumLst - list
    '''
    if len(lst1) == 0 : return []
    cumLst = [lst1[0]]
    for i in range(1,len(lst1)):
        nextElement = cumLst[i-1] + lst1[i]
        cumLst.append(nextElement)
    return cumLst
            
def main():
    '''
    Objective: To find the cumulative sum of elements of the integer list
    Input parameter: None
    Output: None
    '''
    myList = eval(input('Enter the list='))
    result = cumulativeList(myList)
    print('List with cumulative sum::' ,result)

if __name__ == '__main__':
    main()
