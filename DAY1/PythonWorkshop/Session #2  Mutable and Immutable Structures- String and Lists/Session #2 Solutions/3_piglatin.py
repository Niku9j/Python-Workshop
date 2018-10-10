def convertWord(word):
    '''
    Objective: To convert the word to pig latin
    Input Parameter: word
    Return Value: pig latin word
    '''
    '''
    Description of Pig-Latin:
        Pig-Latin takes the first letter of a word, puts it at the end, and
        appends ay. The only exception is if the first letter is a vowel, in
        which case we keep it as it is and append hay to the end.
        E.g. hello -> ellohay, and image -> imagehay
    '''
    '''
    Approach: Extract first letter of word, examine it to form Pig-Latin word
    '''
    first_letter = word[0]
    if first_letter in 'aeiouAEIOU':
        return word + 'hay'
    else:
        return word[1:] + word[0] + 'ay'


def convertSentence(sentence):
    '''
    Objective: To convert text in a sentence to pig latin
    Input Parameter: sentence
    Return Value: Sentence in pig latin
    '''
    '''
    Approach: Split sentence into words and convert each word to pig latin.
    Return the resulted sentence with each word replaced with converted pig
    latin word.
    '''
    list_of_words = sentence.split(' ')
    new_sentence = ''
    for word in list_of_words:
        new_sentence = new_sentence + convertWord(word)
        new_sentence = new_sentence + ' '
    return new_sentence

def main():
    '''
    Objective: To convert text in a sentence to pig latin
    Input parameter: None
    Output: None
    '''
    '''
    Approach: To call function convertSentence
    '''
    text = input('Enter the text to be converted=')
    result = convertSentence(text)
    print('Piglatin Text:: ' + result)

if __name__ == '__main__':
    main()
