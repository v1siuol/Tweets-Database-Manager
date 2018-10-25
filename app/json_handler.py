import ijson
from app.db_models import Tweet

# TODO

print('ues')
# input_path = '../data/1-1-2018.geojson'
input_path = '../data/test.json'
with open(input_path, 'r') as f:
    # parser = ijson.parse(f)


    objects = ijson.items(f, 'posts')
    # objects = ijson.items(f, 'features')

    # print(list(objects)[0])
    for tweets in objects:
        for tweet in tweets:
            print(tweet)
            print(tweet['timestamp'])

    # for i in objects[0]:
    #     _name =
    #     print(i['posts'][0])
    #
    # t = Tweet(user_name=_name,
    #           latitude=_la,
    #           longitude=_lo,
    #           tweet=_tweet,
    #           sentiment=_sentiment,
    #           )