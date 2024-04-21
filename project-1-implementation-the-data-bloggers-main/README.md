## Analysis of Key Factors Influencing TV Shows' Success

## Description

The project collects real-time data from three data sources: Twitter, Reddit, and TMDB. It uses Twitter's sample streaming API to collect one percent sample stream data. For Reddit, it collects domain data from various TV show-related subreddit threads. Finally, for TMDB, four imperative APIs are used to obtain TV show-related data, which updates the database in real time. The Reddit and TMDB APIs are scheduled to run once per day, while the Twitter API will run continuously and store data to MongoDB.



## Team - The Data Bloggers

* Aakarsha LNU, alnu2@binghamton.edu
* Riya Yeshwant Thakur, rthakur1@binghamton.edu
* Ishan Bagchi, ibagchi1@binghamton.edu
* Aayushi Ahlawat, aahlawa1@binghamton.edu
* Tarun Tiwari, ttiwari1@binghamton.edu 

## Tech-stack

* `python` - The project is developed and tested using python. 
* `request` - Request is a popular HTTP networking module(aka library) for python programming language. (2.25.1)
* `MongoDB` - This project uses a non-relational document database that provides support for JSON-like storage for saving collected data. 
* `Flask` - The project uses Flask which is a micro web framework written in Python. (2.2.2)
* `Certifi` - Python SSL Certificates. (2020.6.20)
* `PyMongo` - This project uses python distribution containing tools for working with MongoDB. (4.3.2)
* `Python-dotenv` - It reads key-value pairs from .env file and can set them as environment variables. (2.25.1)
* `flask apsscheduler` - It is a Flask extension which adds support for the APScheduler and schedule reddit api and tmdb_changes api.
* `screen` - It is a  terminal multiplexer used to continuously run the services to fetch data.


## Three data-source documentation

* `Twitter`
  * Twitter Streaming API : "https://api.twitter.com/2/tweets/sample/stream?tweet.fields=context_annotations,geo,author_id,public_metrics,lang,promoted_metrics&expansions=author_id&user.fields=name,username,location" - Real time stream of tweets will be collected using the Streaming API.

* `Reddit` - We are using a list of subreddits:
  * Subreddit_list:['Television','marvelstudios','BetterCallSaul','tvdetails','GameOfThrones','BreakingBad','thewalkingdead','HIMYM','strangerthings','Sherlock',           'DunderMifflin', 'houseofcards','strangerthings', 'bigbrother', 'brooklynninenine', 'riverdale', 'letterkenny','blackmirror', '30rock']
  * [r/subreddit_name] : https://oauth.reddit.com/r/subreddit_name - Real time data will be retrieved from the selected subreddit_list.
 

* `TMDB` - Real time data will be collected from the Movie Database (TMDB), a community-built TV and movie database.
  * [API] : /getalltvshows - Will collect all the TV Shows sorted in descending order wrt their first air date.
  * [API] : /gettvshowsreviews - Will collect individual reviews that would affect the rating of the show.
  * [API] : /gettvshowdetails - Will collect all the details wrt to the TV show.
  * [API] : /gettvchanges - Will store all the changes occurred to the TV shows within the last 24 hours.
  


## How to run the project?

1. Install requirements.txt to install all the dependencies added in the remote server: 
```
   pip install -r requirements.txt
```
2. To launch the scheduler for Reddit and TMDB APIs, run
```
   python3 app.py
```
3. Run the twitter stream using:
```
   python3 twitterstream.py
```
4. Currently both the files are running on two different **screens** to continuously fetch the data.


## Database schema - NoSQL 

<details>
  <summary markdown="span"> collection_1: twitter_stream </summary>

```
{
  'id' : 6360949ca5b49626373f2d99
  'data' : Object
  'includes' : Object
  'tweet_fetched_time' : 2022-10-31T23:38:04.785+00:00
  'tweet' : "RT @mxgnusbxne: heartstopper fandom forced joe locke to deactivate and…"
  'author_id' : "1291248965741051904"
  'tweet_id' : "1587287808808402944"
  'context_annotations' : Array
  'edit_history_tweet_ids' : Array
  'geo' : Object
}
```
</details>

<details>
  <summary markdown="span"> collection_2: reddit </summary>
  
```
{
 {
  "_id": {
    "$oid": "6361b07a11d8208044573dd6"
  },
  "kind": "t3",
  "id": "yfqh0q",
  "subreddit_id": "t5_2qh6e",
  "subreddit": "television",
  "text": "Comments are sorted by new by default.\n\n* Feel free to describe what shows you've been watching and what you think of them.\n\n* Feel free to ask for and give recommendations for what to watch to other users.\n\n* All requests for recommendations are redirected to this thread, however you are free to create your own thread to recommend something to others or to discuss what you're currently watching.\n\n* Use spoiler tags where appropriate. Copy and edit this text: \\&gt;!Spoiler!&lt; becomes &gt;!Spoiler!&lt;. Type *inside* the exclamation marks, with no extra spaces.",
  "author_fullname": "t2_6l4z3",
  "title": "What are you watching and what do you recommend? (Week of October 28, 2022)",
  "subreddit_name_prefixed": "r/television",
  "upvote_ratio": 0.89,
  "domain": "self.television",
  "created_date": {
    "$date": {
      "$numberLong": "1667346554324"
    }
  }
}
}
```
</details>

<details>
  <summary markdown="span"> collection_3: tmdb_tv_shows</summary>
  
```
{
  'id' : 635ff65c93736acd535dc44d
  'backdrop_path' : null
  'first_air_date' : "2024-12-12"
  'genre_ids' : Array
  'id' : 213338
  'name' : "The Buccaneers"
  'origin_country' : Array
  'original_language' : "en"
  'original_name' : "The Buccaneers"
  'overview' : "The Buccaneers adaptation follows a group of fun-loving young American…"
  'popularity' : 0.6
  'poster_path' : null
  'vote_average' : 0
  'vote_count' : 0
   'show_details': {
    'id' : 635ff65c93736acd535dc44d
    'backdrop_path' : null
    'first_air_date' : "2024-12-12"
    'genre_ids' : Array
    'id' : 213338
    'name' : "The Buccaneers"
    'origin_country' : Array
    'original_language' : "en"
    'original_name' : "The Buccaneers"
    'overview' : "The Buccaneers adaptation follows a group of fun-loving young American…"
    'popularity' : 0.6
    'poster_path' : null
    'vote_average' : 0
    'vote_count' : 0
     'show_details': {
        'adult': false,
        'backdrop_path': null,
        'created_by': [
                  {
            'id': 139551,
            'credit_id': '635bafd00c3ec8007904d925',
            'name': 'Katherine Jakeways',
            'gender': 1,
            'profile_path': '/jmYoefPJA449FFBa3pfUyMioKvb.jpg'
                  }
              ],
        'episode_run_time': [],
        'first_air_date': '2024-12-12',
        'genres': [],
        'homepage': '',
        'id': 213338,
        'in_production': true,
        'languages': ['en'
              ],
        'last_air_date': null,
        'last_episode_to_air': null,
        'name': 'The Buccaneers',
        'next_episode_to_air': {
          'air_date': '2024-12-12',
          'episode_number': 1,
          'id': 4029286,
          'vote_average': 0,
          'vote_count': 0
              },
        'networks': [],
        'number_of_episodes': 1,
        'number_of_seasons': 1,
        'origin_country': [
          'US'
              ],
        'original_language': 'en',
        'popularity': 0.6,
        'poster_path': null,
        'production_companies': [],
        'production_countries': [],
        'spoken_languages': [],
        'status': 'In Production',
        'tagline': '',
        'type': 'Scripted',
        'vote_average': 0,
        'vote_count': 0
          }
    }  
  
```
</details>

<details>
  <summary markdown="span"> collection_3: collection_4: tv_show_changes</summary>
  
```    
{
  'id' : 63602b4c58b84aed0f4b871b
  'key' : "name"
  'items' : Array
  '0' : Object
  'id' : "636017473396b9007ad01eb9"
  'action' : "added"
  'time' : "2022-10-31 18:43:19 UTC"
  'iso_639_1' : "he"
  'iso_3166_1' : "IL"
  'tv_id' : 138999
  'created_on' : 2022-10-31T20:08:44.208+00:00
}

  ```
</details>

<details>
  <summary markdown="span"> collection_5: tv_show_reviews</summary>
  
```    
{
  'id' : 635ffa81b6b847a1b3a0e5d3
  'tv_id' : 95403
  'reviews' : Array
  '0' : Object
  'author' : "MovieGuys"
  'author_details' : Object
  'name' : ""
  'username' : "MovieGuys"
  'avatar_path' : null
  'rating' : 5
  'content' : "The real peripheral in this predictably woke series, is men. They are …"
  'created_at' : "2022-10-23T05:19:02.994Z"
  'id' : "6354cec6f8e98200799b0025"
  'updated_at' : "2022-10-23T05:20:56.585Z"
  'url' : "https://www.themoviedb.org/review/6354cec6f8e98200799b0025"
}

```
</details>


