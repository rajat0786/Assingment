#ASSIGNMENT 12



#Q1


what is access token?
An access token is an object that describes the security context of a process or thread

How generate your access token for any API
sign in to developer account
creat a new api
under that go to keys and access token
generate access token



#Q2


google ip address=172.217.15.68
facebook ip address=31.13.69.230


#Q3

import tweepy
from keys import consumer_key,consumer_secret,access_secret,access_token


oauth=tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)
api=tweepy.API(oauth)
print(api.search("#modi"))

#Q4

API is a part of library which defines how an application communicates with external code
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along
with a large collection of high-level mathematical functions to operate on these arrays.


#Q5
import tweepy
from keys import consumer_key,consumer_secret,access_secret,access_token


oauth=tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)
api=tweepy.API(oauth)
user=api.get_user("rajatbh18556917")
print(user.screen_name)
print(user.followers_count)
print(user.friends_count)
print(user.)




