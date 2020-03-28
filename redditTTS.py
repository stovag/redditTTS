import praw
from gtts import gTTS
import os

sub = str(input())
reddit = praw.Reddit(client_id='Your reddit API id', client_secret='Your reddit API secret id', user_agent='Your reddit username')

for submission in reddit.subreddit(sub).new(limit=20):
    title = submission.title
    posttext = submission.selftext
    post = title+"\n"+posttext
    tts = gTTS(text=post, lang='en')
    tts.save("reddit.mp3")
    print(post)
    os.system("mpg123 reddit.mp3")
