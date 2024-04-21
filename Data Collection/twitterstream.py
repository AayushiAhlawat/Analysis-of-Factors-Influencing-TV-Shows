from bson import json_util
from datetime import datetime
from datetime import timedelta
import json
import requests
import pymongo
import certifi
import os
from dotenv import load_dotenv
load_dotenv()

mongo_hostname = os.getenv('MONGO_HOSTNAME')
mongo_portnumber = int(os.getenv('MONGO_PORT_NUMBER'))
client = pymongo.MongoClient(mongo_hostname, mongo_portnumber)
db = client[os.getenv('MONGO_DATABASE_NAME')]

def connect_to_endpoint(url,headers,twittercollection,countcollection):
    try:
        twitter_response = requests.request("GET", url, headers=headers, stream=True)
        for response_line in twitter_response.iter_lines():
            if response_line:
                json_response = json.loads(response_line)
                if('context_annotations' in json_response['data'] and json_response['data']['lang']=="en"):
                    annotations=json_response['data']['context_annotations']
                    for entry in annotations:
                        if entry['domain']['name']=="TV Shows":
                            #print("We got a TV Show Tweet!")
                            current_time = datetime.now()
                            #print(current_time)
                            tweet = parse_json(json_response)
                            tweet['tweet_fetched_time'] = current_time
                            #print(x)
                            try:
                                twittercollection.insert_one(tweet)
                                print("Tweet inserted at {}".format(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
                                print(json.dumps(json_response, indent=4, sort_keys=True))
                            except:
                                print("handling the error")
                                connect_to_endpoint(url, headers, twittercollection,countcollection)
    except Exception as  error:
        print(error)


def twitter_stream_main():
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    url = "https://api.twitter.com/2/tweets/sample/stream?tweet.fields=context_annotations,geo,author_id,public_metrics,lang,promoted_metrics&expansions=author_id&user.fields=name,username,location"
    timeout = 0
    try:
        twitter_collection = db.twitter_stream
        count_collection=db.data_collection_stats
        print("Connected successfully!!!")
    except:
        print('Could not connect to MongoDB')
    while True:
        connect_to_endpoint(url, headers, twitter_collection, count_collection)
        timeout += 1


def count_tweets(start_time,end_time,collection, countcollection):
    #start_date = datetime.strptime(start_time, '%Y-%m-%d')
    #end_date = datetime.strptime(end_time, '%Y-%m-%d')

    count = collection.count_documents({'tweet_fetched_time': {'$gte': start_time,
                                                            '$lt': end_time}})
    print(count)
    data={
        "date":start_time,
        "count": count,
        "source":"twitter"
         }
    countcollection.insert_one(data)

def parse_json(data):
    return json.loads(json_util.dumps(data))


if __name__ == "__main__":
    twitter_stream_main()
