print("****Sharing on Twitter****")

import tweepy
import os
# Authenticate to Twitter
auth = tweepy.OAuthHandler("YOURTWITTERAPI", "YOURTWITTERAPI")
auth.set_access_token("YOURTWITTERAPI", "YOURTWITTERAPI")

# Create API object
api = tweepy.API(auth)

# Number of files in the directory
lista = os.listdir(".")
# Create a tweet
for i in range(len(lista)):
    try:
      api.update_with_media(str(i)+".jpg")
      print("Shared : "+str(i)+".jpg")
    except:
        print("no image called "+str(i)+".jpg")
        pass
    
      

