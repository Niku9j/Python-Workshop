
def wordCount(str1):
    '''
    Objective: To compute the number of words in the input sentence
    Input Parameters: sentence - string
    Return value: None
    ''' 
    words = str1.split(' ')
    count = len(words)
    return count

def main():
    '''
    Objective: To compute the number of words in the sentence provided as input by user
    Input Parameter: None
    Return Value: None
    '''
    sentence = input('Enter plain sentence:')
    numWords = wordCount(sentence)
    print('Number of words in sentence are:', numWords)

if __name__ == '__main__':
    main()
