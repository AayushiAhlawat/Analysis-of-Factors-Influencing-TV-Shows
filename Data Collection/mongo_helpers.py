#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime
from tmdb_config import *
def save_to_mongo(db, data, collection_name, insert_one=True):
    try:
        tmdb_collection = db[collection_name]
        if insert_one:
            return tmdb_collection.insert_one(data)
        return tmdb_collection.insert_many(data)
    except Exception as error:
        print(error)


def get_released_tv_shows(db):
    try:
        tmdb_collection = db.tmdb_tv_shows
        return tmdb_collection.aggregate([
    {
        '$match': {
            'first_air_date': {
                '$ne': ''
            }
        }
    }, {
        '$project': {
            'id': 1, 
            'first_air_date': {
                '$dateFromString': {
                    'dateString': '$first_air_date'
                }
            }
        }
    }, {
        '$match': {
            'first_air_date': {
                '$lt': datetime.now()
            }
        }
    }
])
    except Exception as error:
        print(error)
 

def get_all_tv_show_ids(db):
    try:
        return db.tmdb_tv_shows.find().distinct('id')
    except Exception as error:
        print(error)
 
def update_tv_show_details(db, tv_id, data):
    try:
        return db.tmdb_tv_shows.update_one({"id" : tv_id },{"$set" : {"show_details": data}})
    except Exception as error:
        print(error)

def update_tv_cast(db, tv_id, data):
    try:
        return db.tmdb_tv_shows.update_one({"id" : tv_id },{"$set" : {"credits": data}})
    except Exception as error:
        print(error)

def tv_id_exists(db, tv_id):
    tv_details = list(db.tmdb_tv_shows.find({"id": tv_id}))
    if len(tv_details) > 0:
        return True
    else:
        return False

def update_tv_show_changes(db, tv_show_change):
    try:
        type_array_keys = ['languages', 'origin_country', 'production_companies', 'created_by', 'episode_run_time',  'generas', 'production_countries']
        type_string_keys = ['overview', 'status',  'type', 'name', 'tagline']
        tv_id = tv_show_change['tv_id']
        change_key = tv_show_change['key']
        change_items = tv_show_change['items']
        update_key = tmdb_collection_mappings(change_key)

        if change_key in type_string_keys and len(change_items) > 0:
            update_string_type_keys_tmdb(db, tv_id, change_key, change_items, update_key)
        
        elif change_key in type_array_keys and len(change_items) > 0:
            update_array_type_keys_tmdb(db, tv_id, change_key, change_items, update_key)

        return "Data updated for TV ID : {}".format(tv_id)
    except Exception as e:
        print(e)

def update_array_type_keys_tmdb(db, tv_id, change_key, change_items, update_key):
    for change_item in change_items:
        new_value = change_item['value']
        if change_item['action'] == 'added':
            if type(new_value).__name__ == 'list':
                db.tmdb_tv_shows.update_one({'id': tv_id}, {"$set": {update_key : new_value}})
            else:
                db.tmdb_tv_shows.update_one({'id': tv_id}, {"$push": {update_key : new_value}})
        elif change_item['action'] == 'updated':
            db.tmdb_tv_shows.update_one({'id': tv_id}, {"$set": {update_key : new_value}})
        elif change_item['action'] == 'deleted':
            old_item = change_item['original_value']
            db.tmdb_tv_shows.update_one({'id': tv_id}, {"$pull": {update_key : old_item}})
    
    print("Data updated for key_name: {} and tv_id: {}".format(change_key, tv_id))
    return "Data updated for key_name: {} and tv_id: {}".format(change_key, tv_id)


def update_string_type_keys_tmdb(db, tv_id, change_key, change_items, update_key):
    #filter for overview and name for english language
    if change_key in ['overview', 'name']:
        change_items = [change for change in change_items if change['iso_639_1'] == 'en' and change['iso_3166_1'] == 'US']
    if len(change_items) > 0:
        latest_item = change_items.pop()
        new_value = latest_item.get('value')
        if new_value:
            db.tmdb_tv_shows.update_one({'id': tv_id}, {"$set": {update_key : new_value}})
    print("Data updated for key_name: {} and tv_id: {}".format(change_key, tv_id))
    return "Data updated for key_name: {} and tv_id: {}".format(change_key, tv_id)
    