# COMMENTS

* Overall, the ideas are fine.
* How often is TMDB going to update?
* Don't use any search or filter paramters. You need to receive the entire 1% stream so you can answer how many tweets per day. Only keep the tweets you are interested in.

# NOTES FROM 1:1

* Can the TMBD thing be run any more frequently than 24 hours.
* Do some testing and see how often things are changing in TMDB. Get 24 hours of content, then see how many new items there are, then divide by 24 (that gives per hour), then another 60 (that gives per minute).
* Depending on what the above looks like, let's try to tune the TMDB crawler to run more frequently than every 24 hours. I.e., how often you run it. Every 24 hours hours, every 12 hours, every 10 minutes, etc.
