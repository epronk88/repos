def parser():
    import feedparser
    import tweepy
    import time
    from datetime import datetime
    import pytz


    fmt = "%d-%b-%Y (%H:%M:%S)"
    
    # Converting datetime object to string
    dateTimeObj = datetime.now(pytz.timezone('Europe/Berlin'))
    timestampStr = dateTimeObj.strftime(fmt) 
    print('Current Timestamp : ', timestampStr)

    key = "1RDuYkSifw5wA0BGivxWMuZv1"
    keySecret = "lz3XKEoNoGCR9wNKDvAWDAGxI9E1cJ9zvYRGq0eNAKfvlyJ81Z"
    accessToken = "1093072820-yqh9ZaSSv49AMsxf24SC1N8wOEjQVVKbPJclw0X"
    accessTokenSecret = "1taOcANQ08iGeXf75ISaX7XSzG1omlzmO0T8nLBsjkHYN"
    bearer_token=None
    client = tweepy.Client(bearer_token,key,keySecret,accessToken,accessTokenSecret)
    

    feed = feedparser.parse("https://alarmeringen.nl/feeds/region/rotterdam-rijnmond.rss").entries

    
    f = open("last.txt", "r")
    inlezen = f.read()

    matches = ["ambu", "U bent", "proefalarm", "posten", "b1", "b2"]

    for q in range(0, -1, -1):

        time.sleep(3)

        if inlezen != feed[q].title and not any(word in feed[q].title for word in matches):
            #print(feed[q])
            my_datetime_str = feed[q].published

            #print (my_datetime_str)

            my_datetime_object = datetime.strptime(my_datetime_str, "%a, %d %b %Y %H:%M:%S %z")

            my_datetime_local = my_datetime_object.astimezone(pytz.timezone('Europe/Berlin')).strftime('%a, %d %b %Y %H:%M:%S %z')

            #print (my_datetime_local)




            final_new = my_datetime_local [0:25] + '\n' + feed[q].title + '\n' + '#p2000 #rijnmond'

            print(final_new)

            response = client.create_tweet(text=final_new)

            f = open('last.txt', 'w')
            f.write(feed[0].title)
            f.close()

parser()
