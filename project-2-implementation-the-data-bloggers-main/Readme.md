## Analysis of Key Factors Influencing TV Shows' Success

## Description

* For this project, we have thought about and have answered three research questions/areas based on our datasets and the type of data
we have gathered. Our research objectives shall revolve around the factors influencing the popularity of TV shows based on data
collected from TMDB, Twitter and Reddit. 
* Further, we have answered the following research questions:
Ques. How are elements like the genre, cast, number of seasons, number of episodes, production firms, networks, and length of the episodes affecting the success of TV shows?
* From the TMDB data analysis it could be figured out that top 5 features that most affect the success of TV Shows are : returning series status, plot status, ended features status, canceled feature status and in production status with impact of greater than 2.0.And the least important feature is genre erotic with an impact of approximately 0.01.
Ques. To what extent are popular TV series on TMDB hyped on Twitter, and if this hype is positive or negative?
* On the basis of tweet frequency top 20 TV Shows were retrieved to calculate the polarity of each of the show. After
calculating the polarity score hype was marked as positive, negative or neutral hype. On the basis of analysis made
positive and negative hypes were in the range of 0-2000 with highest positive hype at 6000 and negative hype at
2000 respectively.
Ques. What phrases/terms from major TV series are becoming popular and most used or admired by the public on their respective
subreddits?
* From the subreddit analysis 5 major phrases which are becoming popular are: BigBrother, thewalkingdead, HouseOfCards, brooklynninenine, television.

## Team - The Data Bloggers

* Aakarsha LNU, alnu2@binghamton.edu
* Riya Yeshwant Thakur, rthakur1@binghamton.edu
* Ishan Bagchi, ibagchi1@binghamton.edu
* Aayushi Ahlawat, aahlawa1@binghamton.edu
* Tarun Tiwari, ttiwari1@binghamton.edu 


## Methodology for Data Analysis

* `Twitter`
  *  For twitter dataset, tweets related to TV shows were fetched from the data stored in MongoDB followed by storing it in
pickle file.
  *  Descriptive Analysis was performed on the retrieved data to identify various patterns followed in the dataset and a
time series graph was plotted between the tweet count and TV Shows tweet frequency count for a particular duration.
  *  Pre-processing of tweets was done using a pre-processor library in python which includes cleaning, tokenizing, and
parsing of URLs, Hashtags, Mentions, Reserved words (RT,FAV), Emojis and Smileys.
  *  Further, top 100 TV shows were fetched to determine their hype on twitter and number of tweets for a mentioned TV
show was counted followed by its frequency.
  *  For each of the selected TV show polarity score (positive, negative, or neutral) was calculated based on the tweets
and hype was determined based on the polarity score.
  *  And lastly the result was visualized graphically.


* `Reddit` 
  *  For each of the subreddit data stored Top 3,4 phrases were retrieved followed by formation of data frame. Further for descriptive analysis, number of comments for each of the subreddits was retrieved.
  *  Also, analysis for the number of comments for the top 5 subreddit.
  *  Lastly, data analysis was done for the politics subreddit and a time series was plotted to for determining the comments
on a particular date.

 
* `TMDB` 
  *  For TMDB, firstly a connection is established with MongoDB to retrieve and start with the pre-processing of the available data.
  *  In the formed dataframe, the dependent and independent variables were as follows:
  * Independent Variable: id,name,first_air_date,genre,cast_details,episode_run_time,number_of_episodes,number_of_seasons,overview,production_companies,status,type
  * Dependent Variable: popularity
  *  After formation of dataframe, pre-processing is done. 
  *  For Data Preprocessing, firstly Data Cleaning was done in which null, missing and duplicates values were eliminated and One Hot Encoding Technique was used for the categorical data to improve the data accuracy. 
  *  After the pre-processing, model training and testing was done for the data frame which contains 58 columns.
  *  Data frame was divided into training and testing sets and supervised learning modelling was used in which a training set is used to instruct models to produce the desired results. This training dataset has both the right inputs and outputs, enabling the model to develop over time. Further, the technique that was used for modelling under supervisedlearning is “Linear Regression” which is used to find target value based on independent factors.
  * After which graphs are plotted to predict the popularity based on other independent factors.

  





