import praw

reddit = praw.Reddit(
    client_id="g_AEyt0e2wN8o7FPA4_IIQ",
    client_secret="j3xBqbUvi5P0xEhscNoy4waXELLqJw",
    user_agent="re-editv2"
)

subreddit = reddit.subreddit("stories")

top_post = subreddit.hot(limit=5)


for sub in top_post:
    title = sub.title
    
    fileTitle = open(sub.title+".txt")
    