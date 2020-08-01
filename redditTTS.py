import praw
from gtts import gTTS
import os

sub = str(input("Select subreddit:  "))

#  Create the reddit API object
reddit = praw.Reddit(client_id='Your reddit API id', client_secret='Your reddit API secret id', user_agent='Your reddit username') 

limit = int(input("Number of posts to read: "))

for submission in reddit.subreddit(sub).new(limit=limit):
    title = submission.title
    posttext = submission.selftext
    post = title+"\n"+posttext
    tts = gTTS(text=post, lang='en')
    tts.save("reddit.mp3")
    print(post)
    os.system("mpg123 reddit.mp3")
    
os.remove("reddit.mp3")
