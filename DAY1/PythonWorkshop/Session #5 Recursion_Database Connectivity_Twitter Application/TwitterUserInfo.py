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

def getUserStatistics(user):
    '''
    Objective: To get user statistics using various
            variables of the api
    Input Parameter: user - string
    Return Value: None
    '''
    print('\nName: ', user.name)
    print('Screen Name: ', user.screen_name)
    print('ID: ', user.id)
    print('Account creation date and time: ', user.created_at)
    print('Location: ', user.location)
    print('Description: ', user.description)
    print('No. of followers: ', user.followers_count)
    print('No. of friends: ', user.friends_count)
    print('No. of favourite tweets: ', user.favourites_count)
    print('No. of posted tweets: ', user.statuses_count)
    print('Associated URL: ', user.url)

def main():
    '''
    Objective: To collect user information
    Input Parameter: None
    Return Value: None
    '''
    # To print user's information
    api = OAuthVerifier()
    # Authenticated User
    user = api.me()
    getUserStatistics(user)

if __name__ == '__main__':
    main()
