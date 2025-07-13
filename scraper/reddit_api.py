from praw.models import MoreComments

def get_user_data(username):
    import praw
    import os
    from dotenv import load_dotenv
    load_dotenv()

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    user = reddit.redditor(username)
    
    posts = []
    comments = []

    for submission in user.submissions.new(limit=None):
        cleaned = submission.selftext.strip() or "[removed]"
        posts.append(
            f"[POST by u/{username}]\nTitle: {submission.title}\nText: {cleaned}\nSubreddit: r/{submission.subreddit}\n"
        )


    for comment in user.comments.new(limit=None):
        cleaned = comment.body.strip() or "[removed]"
        comments.append(
            f"[COMMENT by u/{username}]\n{cleaned}\nSubreddit: r/{comment.subreddit}\n"
        )

    return posts + comments
