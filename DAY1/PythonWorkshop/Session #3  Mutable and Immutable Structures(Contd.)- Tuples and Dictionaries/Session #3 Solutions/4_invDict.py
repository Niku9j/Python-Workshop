def buildInvDict(dict1):
    '''
    Objective: To construct an inverted dictionary
    Input Parameter: dict1 : dictionary
    Return Value: invDict : dictionary
    '''
    '''
    Approach:
    For every key-value pair of word:meaning in the dictionary dict1,
    if it is the first occurrence meaning, then add  meaning:[word] 
    in the inverted dictionary.
    If the key meaning already exists in the inverted dictionary,
    then append the word to the list invDict[meaning].
    '''
    invDict = {}
    for key,value in dict1.items():
        if value in invDict:
            invDict[value].append(key)
        else:
            invDict[value] = [key]
    return invDict

def main():
    '''
    Objective: To find inverted dictionary
    Input Parameter: None
    Return Value: None
    '''
    wordMeaning = eval(input('Enter word meaning dictionary: '))
    meaningWord = buildInvDict(wordMeaning)
    print('Inverted Dictionary:\n', meaningWord)

# Statements to initiate the call to main function.
if __name__ == '__main__':
    main()
