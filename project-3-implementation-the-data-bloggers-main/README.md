## Analysis of Key Factors Influencing TV Shows' Success

## Description

* For this project, we have created an interactive dashboard that will be updated in real-time, showing results for the below three research questions/areas
 based on our datasets and the type of data we have gathered. Our research objectives shall revolve around the factors influencing the popularity of TV 
shows based on data collected from TMDB, Twitter and Reddit.
* Further, the following are the research questions: <br/> 
**Ques. How are elements like the genre, cast, number of seasons, number of episodes, production firms, networks, and length of the episodes affecting the success of TV shows?** <br/>
**==>** From the TMDB data analysis it could be figured out that top 5 features that most affect the success of TV Shows are : returning series status, plot status, ended features status, canceled feature status and in production status with impact of greater than 2.0.And the least important feature is genre erotic with an impact of approximately 0.01. <br/>
**Ques. To what extent are popular TV series on TMDB hyped on Twitter, and if this hype is positive or negative?** <br/>
**==>** On the basis of tweet frequency top 20 TV Shows were retrieved to calculate the polarity of each of the show. After
calculating the polarity score hype was marked as positive, negative or neutral hype. On the basis of analysis made
positive and negative hypes were in the range of 0-2000 with highest positive hype at 6000 and negative hype at
2000 respectively. <br/>
**Ques. What phrases/terms from major TV series are becoming popular and most used or admired by the public on their respective
subreddits?** <br/>
**==>** From the subreddit analysis 5 major phrases which are becoming popular are: BigBrother, thewalkingdead, HouseOfCards, brooklynninenine, television.

## Team - The Data Bloggers

* Aakarsha LNU : alnu2@binghamton.edu
* Riya Yeshwant Thakur : rthakur1@binghamton.edu
* Ishan Bagchi : ibagchi1@binghamton.edu
* Aayushi Ahlawat : aahlawa1@binghamton.edu
* Tarun Tiwari : ttiwari1@binghamton.edu 

## TMDB

* TMDB  is a website where users may discover millions of moviesand TV episodes. It gives us the option to look for the most well liked films or 
TV shows that are now being seen in cinemas, on TV, or that are available for rental. Users of the portal can also publish reviews of movies and TV series 
and rate them. The website offers suggestions depending on the movies the user has looked up or seen.

## Twitter

* Twitter is an open social network that people use to converse with each other in short messages, known as tweets. People publish their
comments regarding actors, production companies, and TV shows, which is useful for our study of the most popular and trending
shows and their dependence on various factors.

## Reddit

* Reddit is a social news aggregation, content review, and debateplatform. The website’s material, which includes links, text entries, photographs,
and videos, is contributed by registered users and is then rated by other users. Posts are arranged into user-made boards called "communities" 
or "subreddits" according to their subjects. When there are enough upvotes, posts that have received the most upvotes will eventually appear on 
the first page of the website.

## DASH Library

* The original low-code framework, Dash, allows users to create data apps quickly in Python, R, Julia, and F (experimental).
* Dash is the best tool for creating and delivering data apps with unique user interfaces because it was built on top of Plotly.js and React.js. 
It is especially appropriate for anyone who handles data.
* Dash abstracts away all the technologies and protocols necessary to create a full-stack web app with interactive data visualization using 
a few straightforward principles.

## Methodology for Live Dashboard

* For this project, we have created an interactive dashboard that updates in real-time, showing results for the above-mentioned research questions.
* The dashboard is implemented using the Flask framework, and all the plots and graphs are built using various Python libraries.
* Further functionality to filter the results, based on the query entered by the user in our dashboard is added.
* The Dash HTML Components module (dash.html) has a component for every HTML tag as well as keyword arguments for all of the HTML arguments.
* TMDB Dataframe is converted into a csv file named predictions.csv using which a layout have been using DASH library to display the graph for 
Popularity Predictions for the Un-Released TV Shows.
* For reflecting the twitter data and , dataframe made for twitter is converted into showspolarity.csv, showing the analysis of Hype of the most popular TMDB TV shows on Twitter.
* Similarly for reddit, after converting dataframe into csv files named class.csv and datecom.csv, DASH library was used to show the graph for Number of Posts by each subreddit 
and a time series graph.




  






