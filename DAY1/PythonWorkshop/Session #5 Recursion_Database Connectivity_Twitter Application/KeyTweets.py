import tweepy

def OAuthVerifier():
    '''
    Objective: To authorize the application to access Twitter
    Input Parameter: None
    Return Value: API object
    '''
    consumerKey = 'iym0XRG0SOgyPOjmlPQgB4XrC'
    consumerSecret = 'I6gBj8RpcXJvN6xaKUUGeTkPEDpHziRXBmT9d9yG8k5Ik0H0bF'
    authorization = tweepy.OAuthHandler(consumerKey, consumerSecret)
    accessToken = '727494459118653446-XWf9MmBJmCUOM7Ic9xvoHlZCBQAWWA1'
    accessSecret = 'jl4UJPXYSC8ygV8EsyNz6fMOW2NEs9NFvJc2InyfXNvve'
    authorization.set_access_token(accessToken, accessSecret)
    api = tweepy.API(authorization)
    return api

class MyStreamListener(tweepy.StreamListener):
    # Class inheriting StreamListener of tweepy module

    def on_status(self, status):
        '''
        Objective: To print text stream of tweets
        Input Parameters:
            self (implicit parameter) - object of type
            MyStreamListener
            status - string value representing tweet
        Return Value: None
        '''
        import sys
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        print(status.text.translate(non_bmp_map))
    
    def on_error(self, status):
        '''
        Objective: To disconnect the stream by returning False
        if error 420 occurs
        Input Parameters:
            self (implicit parameter) - object of type
            MyStreamListener
            status - int value representing error code
        Return Value: result - int
        '''
        if status==420:
            return False

def main():
    '''
    Objective: To print streaming data containing given keywords
    Input Parameter: None
    Return Value: None
    '''
    api = OAuthVerifier()
    # Creates a stream listener object listenerOb
    listenerOb = MyStreamListener()
    # Create a Stream object
    myStream = tweepy.Stream(api.auth, listenerOb)
    # Starts streaming by specifying search keywords
    searchList = eval(input('Enter search keywords list: '))
    myStream.filter(track = searchList)

if __name__ == '__main__':
    main()
