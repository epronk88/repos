def parser():
    import feedparser
    import tweepy
    from datetime import datetime
    import pytz


    fmt = "%d-%b-%Y (%H:%M:%S)"
    
    # Converting datetime object to string
    dateTimeObj = datetime.now(pytz.timezone('Europe/Berlin'))
    timestampStr = dateTimeObj.strftime(fmt) 
    print('Current Timestamp : ', timestampStr)

    consumer_key = "xZLVPRB4Is6mfjyKijKxg"
    consumer_secret = "khMjfOvrjmDDcjZxNzGq9qTPlMQ0ERaIP5WhJJ9lo"
    access_token = "1093072820-AJFCrrUNKUALq2wUMakAJ5E89rGqXA4OLSfxTVx"
    access_token_secret = "0vuslRTeqh3buaQPylBia1JKH1qA3TksrEnPQEm9NeVHu"

    
    

    
    
    feed = feedparser.parse("https://alarmeringen.nl/feeds/region/rotterdam-rijnmond/politie.rss").entries
    
    
    f = open("/app/last.txt", "r")
    inlezen = f.read()

    if inlezen != feed[0].title:
        
        #print(feed[0])
        my_datetime_str = feed[0].published

        print (my_datetime_str)

        my_datetime_object = datetime.strptime(my_datetime_str, "%a, %d %b %Y %H:%M:%S %z")

        my_datetime_local = my_datetime_object.astimezone(pytz.timezone('Europe/Berlin')).strftime('%a, %d %b %Y %H:%M:%S %z')

        print (my_datetime_local)




        final_new = my_datetime_local [0:25] + '\n' + feed[0].title

        print(final_new)

        def OAuth():
                    try:
                        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
                        auth.set_access_token(access_token, access_token_secret)
                        return auth

                    except Exception as e:
                        return None 
        
        oauth = OAuth()
        api = tweepy.API(oauth)
        api.update_status(final_new)
        print('A tweet is posted')


    f = open('/app/last.txt', 'w')
    f.write(feed[0].title)
    f.close()

parser()
