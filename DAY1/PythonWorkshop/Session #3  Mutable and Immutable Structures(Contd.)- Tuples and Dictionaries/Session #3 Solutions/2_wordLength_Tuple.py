def wordLength(list1):
    '''
    Purpose: To return word-length pair for each word given in the list.
    Input Parameter: list1 - list containing words
    Return Value: List of tuples containing word and its length
    '''
    '''
    Approach:
    For each word in list1:
            Append a tuple containing word and its length to the list.
    '''
    wordLength = list()
    for word in list1:
        wordLength.append((word, len(word)))
    return wordLength


def main():
    '''
    Purpose: For each word given in list, return a list of tuples containing
    word and its length.
    Input Parameter: None
    Return Value: None
    '''
    list1 = eval(input('Enter the list: '))
    print('List of tuples:: ', wordLength(list1))

if __name__ == '__main__':
    main()
