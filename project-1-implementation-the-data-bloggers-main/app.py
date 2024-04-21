#!/usr/bin/env python
# encoding: utf-8
from datetime import date, timedelta
import json
from flask import Flask, request, jsonify
import requests
import pymongo
import certifi
from mongo_helpers import *
from dotenv import load_dotenv
import os
load_dotenv()
from flask_apscheduler import APScheduler
from reddit import get_subreddit_data, get_politics_subreddit_count

app = Flask(__name__)

mongo_hostname = os.getenv('MONGO_HOSTNAME')
mongo_portnumber = int(os.getenv('MONGO_PORT_NUMBER'))
client = pymongo.MongoClient(mongo_hostname, mongo_portnumber)
db = client[os.getenv('MONGO_DATABASE_NAME')]
base_url = os.getenv('TMDB_BASE_URL')
api_key = os.getenv('TMDB_API_KEY')


def get_tv_changes():
    try:
        tv_change_list_url = base_url+ "tv/changes"+ "?api_key=" + api_key + "&language=en-US&page=1"
        tv_change_list_response = requests.get(tv_change_list_url).json()
        if 'results' in tv_change_list_response and len(tv_change_list_response['results']) > 0:
            tv_change_list = tv_change_list_response['results']
            for tv_details in tv_change_list:
                tv_id = tv_details['id']
                if tv_id_exists(db, tv_id):
                    tv_change_url = base_url+ "tv/" + str(tv_id) + "/changes"+ "?api_key=" + api_key
                    tv_change_response = requests.get(tv_change_url).json()
                    tv_show_changes =  tv_change_response['changes']
                    valid_keys = ['languages', 'origin_country', 'overview', 'production_companies', 'status',  'type', 'created_by', 'episode_run_time',  'generas', 'name', 'production_countries', 'tagline']
                    for tv_change in tv_show_changes:
                        if tv_change['key'] in valid_keys:
                            tv_change['tv_id'] = tv_id
                            tv_change['created_on'] = datetime.now()
                            save_to_mongo(db, tv_change, 'tv_show_changes')
                            update_tv_show_changes(db, tv_change)
                else:
                    tv_show_details_url =  base_url+ "tv/" + str(tv_id) + "?api_key=" + api_key + "&language=en-US&page=1"
                    tv_show_response = requests.get(tv_show_details_url).json()
                    if tv_show_response:
                        tv_show_details = {"id": tv_id, 'show_details': tv_show_response}
                        save_to_mongo(db, tv_show_details, 'tmdb_tv_shows')
                        print("New movie details with tv_id {} added to the database".format(tv_id))
            return "All tv changes are updated for date: {}".format(datetime.now)
    except Exception as error:
        print(error)


@app.route('/getalltvshows', methods=['GET'])
def get_all_tv_shows():
    try:
        db.tmdb_tv_shows.create_index('id', unique = True)    
        discover_url = base_url + "discover/tv?api_key=" + api_key
        get_tv_response = requests.get(discover_url).json()
        for page_number in range (1, 501):
            discover_url_based_on_page = base_url + "discover/tv?api_key=" + api_key + "&page=" + str(page_number) + "&sort_by=first_air_date.desc"
            get_tv_response = requests.get(discover_url_based_on_page).json()
            if get_tv_response['results']:
                tv_show_results_list = get_tv_response['results']    
                save_to_mongo(db, tv_show_results_list, 'tmdb_tv_shows', False)
                print("Data successfully stored for page: ", page_number, "\n")
        return "All TV shows data is stored"
    
    except Exception as error:
        print(error)


@app.route('/gettvshowsreviews', methods=['GET'])
def get_tv_shows_reviews():
    try:
        all_tv_shows = get_released_tv_shows(db)
        all_tv_shows = list(all_tv_shows)
        if all_tv_shows:
            for tv_show in all_tv_shows:
                tv_id = tv_show['id']
                tv_reviews_url =  base_url+ "/tv/" + str(tv_id) + "/reviews?api_key=" + api_key + "&language=en-US&page=1"
                get_tv_review_response = requests.get(tv_reviews_url).json()
                if 'results' in get_tv_review_response and len(get_tv_review_response['results']) > 0:
                    tv_show_results_list = get_tv_review_response['results']
                    tv_show_review = {'tv_id': tv_id, 'reviews' : tv_show_results_list }
                    save_to_mongo(db, tv_show_review, 'tv_show_reviews' )
                    print("Review for TV ID: ", tv_id, "is saved")
                else:
                    print("No reviews for TV ID: ", tv_id)
            return "All tv show reviews are saved."
    except Exception as e:
        print(e)

@app.route('/gettvshowcast', methods=['GET'])
def get_tv_show_cast():
    try:
        all_tv_shows_ids = get_all_tv_show_ids(db)
        if len(all_tv_shows_ids) > 0:
            for tv_id in all_tv_shows_ids:
                tv_show_cast_url = base_url+ "tv/" + str(tv_id) + "/credits?api_key=" + api_key + "&language=en-US"
                tv_cast_response = requests.get(tv_show_cast_url).json()
                if tv_cast_response:
                    update_tv_cast(db, tv_id, tv_cast_response)
                    print("Tv Cast details for TV ID: ", tv_id, "are saved")
                else:
                    print("No Cast details found for TV ID: ", tv_id)
            return "All tv show details are saved."
    except Exception as e:
        print(e)



@app.route('/gettvshowdetails', methods=['GET'])
def get_tv_show_details():
    try:
        all_tv_shows_ids = get_all_tv_show_ids(db)
        if len(all_tv_shows_ids) > 0:
            for tv_id in all_tv_shows_ids:
                tv_show_details_url = base_url+ "tv/" + str(tv_id) + "?api_key=" + api_key + "&language=en-US&page=1"
                tv_show_response = requests.get(tv_show_details_url).json()
                if tv_show_response:
                    update_tv_show_details(db, tv_id, tv_show_response)
                    print("Tv details TV ID: ", tv_id, "are saved")
                else:
                    print("No details found for TV ID: ", tv_id)
            return "All tv show details are saved."
    except Exception as e:
        print(e)


if __name__ == "__main__":
    scheduler = APScheduler()
    scheduler.add_job(id='TV Show Changes TMDB', func=get_tv_changes, trigger='cron', hour='13', minute='30')
    scheduler.add_job(id='Reddit', func=get_subreddit_data, trigger='cron', hour='11', minute='30')
    scheduler.add_job(id='Politics subreddit', func=get_politics_subreddit_count, trigger='interval', minutes= 60)

    scheduler.start()
    app.run(debug=False)