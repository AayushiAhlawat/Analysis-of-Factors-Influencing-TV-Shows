from datetime import datetime, timedelta, date
import json
from flask import Flask, request, jsonify
import requests
import pymongo
import certifi
from mongo_helpers import *
from dotenv import load_dotenv
import os
from flask_apscheduler import APScheduler
load_dotenv()

mongo_hostname = os.getenv('MONGO_HOSTNAME')
mongo_portnumber = int(os.getenv('MONGO_PORT_NUMBER'))
client = pymongo.MongoClient(mongo_hostname, mongo_portnumber)
db = client[os.getenv('MONGO_DATABASE_NAME')]
def get_reddit_auth():
    client_id = os.getenv('REDDIT_CLIENT_ID')
    secret_key = os.getenv('REDDT_SECRET_KEY')
    username = os.getenv('REDDIT_USERNAME')
    password = os.getenv('REDDIT_PASSWORD')
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    data = {'grant_type': 'password',
            'username': username,
            'password': password}
    headers = {'User-Agent': 'MyBot/0.0.1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    return headers

def get_subreddit_data():
    try:
        headers = get_reddit_auth()
        subreddit_list = ['television','marvelstudios','BetterCallSaul','tvdetails','GameOfThrones','BreakingBad','thewalkingdead','HIMYM','strangerthings','Sherlock','DunderMifflin','houseofcards','strangerthings','bigbrother','brooklynninenine','howyoudoin','riverdale','letterkenny','blackmirror','30rock']
        for subreddit in subreddit_list:
            url = os.getenv('REDDIT_REQUEST_URL') + subreddit
            response = requests.request("GET", url, headers=headers).json()
            reddit_data = response['data']['children']
            final_reddits = []
            for each_reddit in reddit_data:
                filtered_data = get_subreddit_fields(each_reddit)
                final_reddits.append(filtered_data)
            save_to_mongo(db, final_reddits, 'reddit', False)
            print("data stored for subreddit {}".format(subreddit))
        return "Data Stored In Reddit"
    except Exception as error:
        print(error)
        pass


def get_politics_subreddit_count():
    try:
        headers = get_reddit_auth()
        subreddit = 'politics'
        url = os.getenv('REDDIT_REQUEST_URL') + subreddit
        response = requests.request("GET", url, headers=headers).json()
        reddit_data = response['data']['children']
        current_politics_subreddit_count = db.reddit.count_documents({'subreddit': 'politics'})
        final_reddits = []
        for each_reddit in reddit_data:
            filtered_data = get_subreddit_fields(each_reddit)
            final_reddits.append(filtered_data)
        save_to_mongo(db, final_reddits, 'reddit', False)
        new_politics_subreddit_count = db.reddit.count_documents({'subreddit': 'politics'})
        new_politics_submissions = new_politics_subreddit_count - current_politics_subreddit_count
        current_date = datetime.combine(datetime.today(), datetime.min.time())
        current_date_politics_stats = db.data_collection_stats.find_one({'dataset': 'reddit', 'subreddit': 'politics', 'created_date': current_date})
        timestamp = datetime.now()
        if current_date_politics_stats:
            new_value = {'timestamp' : timestamp, 'count' : new_politics_submissions }
            db.data_collection_stats.update_one({'dataset': 'reddit', 'subreddit': 'politics', 'created_date': current_date}, {"$push": {'submissions': new_value}})
        else:
            new_value = {'dataset': 'reddit', 'subreddit': 'politics', 'created_date': current_date , 'submissions': [{'timestamp' : timestamp, 'count' : new_politics_submissions }]}
            db.data_collection_stats.insert_one(new_value)
        print("Data stored for subreddit {} and stats updated for date {} and timestamp {}".format(subreddit, current_date, timestamp))
        return "Data Stored In Reddit"
    except Exception as error:
        print(error)
        pass
    

def get_subreddit_fields(each_reddit):
    filtered_data = {
                    'kind': each_reddit.get('kind', ""),
                    "id" : each_reddit.get('data', {}).get('id'),
                    "subreddit_id": each_reddit.get('data', {}).get('subreddit_id'),
                    "subreddit": each_reddit.get('data', {}).get('subreddit'),
                    "text": each_reddit.get('data', {}).get('selftext'),
                    "author_fullname": each_reddit.get('data', {}).get('author_fullname'),
                    "title": each_reddit.get('data', {}).get('title'),
                    "subreddit_name_prefixed": each_reddit.get('data', {}).get('subreddit_name_prefixed'),
                    "upvote_ratio": each_reddit.get('data', {}).get('upvote_ratio'),
                    "domain": each_reddit.get('data', {}).get('domain'),
                    "created_date": datetime.now()
                }
    
    return filtered_data
