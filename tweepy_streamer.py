from  tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


from setting import CONSUMER_KEY , CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth  =OAuthHandler(  CONSUMER_KEY , CONSUMER_SECRET)
        auth.set_access_token( ACCESS_TOKEN , ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer():
    def  __init__(self) -> None:
        self.twitter_authenticator = TwitterAuthenticator()
    
    def stream_tweets(self , fetched_tweets_filename , hash_tag_list):
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app() 
        stream = Stream(auth, listener,verify=False)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)

class TwitterListener(StreamListener):

    def __init__(self , fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data( self ,data):
        try:
            with open(self.fetched_tweets_filename ,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data %s" % str(e))
            return True

    def on_Error(self, status):
        print (status)



if __name__ == "__main__":
    # listner = StdOutListner()
    # auth  =OAuthHandler(  twitter_credentials.CONSUMER_KEY , twitter_credentials.CONSUMER_SECRET)
    # auth.set_access_token( twitter_credentials.ACCESS_TOKEN , twitter_credentials.ACCESS_TOKEN_SECRET)

    hash_tag_list = ["donal trump", "hillary clinton", "barack obama", "bernie sanders"]
    fetched_tweets_filename = "tweets.txt"
    auth = TwitterAuthenticator().authenticate_twitter_app()

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list)
    # stream.filter(track=['bitcoin'])
