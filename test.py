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

    consumer_key = "SvhVUXH5cc7yA7lNbHQRTj0IJ"
    consumer_secret = "zap5PSIdtzZ6kj4BqpZEcBuz9FdDNwRp7inFuwTFZt3HhJtAHF"
    access_token = "1093072820-KngKSFbfn82fhXtLwtQwDlCBBj6oyOIVvpj6QTk"
    access_token_secret = "cJeN996nsaP6Rq2XvR0AOeUcQNvuZnimLmwi1EFF9qoez"

    
    

    
    
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
