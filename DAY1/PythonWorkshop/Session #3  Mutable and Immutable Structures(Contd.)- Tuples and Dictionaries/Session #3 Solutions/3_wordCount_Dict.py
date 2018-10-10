def wordCountDict(list1):
    '''
    Objective: To determine word count from words given in list.
    Input Parameter: list1 - list containg words
    Return Value: wordCount - Dictionary containing the words and its count
    '''
    '''
    Approach:
    For each word w in list
          If w is in dictionary, increment its value
          Else add w to the dictionary with 1 as its value.
    '''
    wordCount = dict()
    for w in list1:
        if w in wordCount:
            wordCount[w] += 1
        else:
            wordCount[w] = 1
    return wordCount

def main():
    '''
    Objective: To determine word count from words given in list.
    Input Parameter: None
    Return Value: None
    '''
    list1 = eval(input('Enter the list: '))
    wordCount1 = wordCountDict(list1)
    print('Dictionary of word count:: ', wordCount1)


if __name__ == '__main__':
    main()
