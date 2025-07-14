from praw.models import MoreComments
import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_user_data(username):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    user = reddit.redditor(username)
    
    posts = []
    comments = []

    for submission in user.submissions.new(limit=None):
        posts.append({
            "type": "post",
            "title": submission.title.strip(),
            "text": submission.selftext.strip() if submission.selftext else "[removed]",
            "subreddit": str(submission.subreddit),
            "url": f"https://reddit.com{submission.permalink}",
            "id": submission.id,
        })

    for comment in user.comments.new(limit=None):
        comments.append({
            "type": "comment",
            "body": comment.body.strip() if comment.body else "[removed]",
            "subreddit": str(comment.subreddit),
            "url": f"https://reddit.com{comment.permalink}",
            "id": comment.id,
        })

    return posts + comments
