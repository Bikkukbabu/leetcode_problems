-- Write your PostgreSQL query statement below
SELECT tweet_id  
from Tweets
where LENGTH(content) > 15;