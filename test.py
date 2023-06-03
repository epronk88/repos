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

    client = tweepy.Client(consumer_key="973MzJmk6AWYd30L62I7pd0x1",
                    consumer_secret="V5gzRtGYwcXiKJpMKc9UHXIGFAjLV6SIRXIQ1W1ny6kO54u8fF",
                    access_token="1093072820-GS3A5QIHfylFAVa1pbl66gwsHVk2Q8uskhiUGpa",
                    access_token_secret="tab4kD9Sfp713jeEpjBzFe8waLrdXhzXcULAEw48xFgDq")

    
    

    
    
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




        final_new = my_datetime_local [0:25] + '\n' + feed[0].title + '\n' + '#p2000 #rijnmond'

        print(final_new)

        response = client.create_tweet(text=final_new)

    f = open('/app/last.txt', 'w')
    f.write(feed[0].title)
    f.close()

parser()
