import praw

# Set up Reddit API access
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent=''
)

# Choose subreddit
subreddit = reddit.subreddit('AskReddit')

# Extract post titles
titles = [submission.title for submission in subreddit.hot(limit=300)]  # Fetch 300 hot posts

# Save titles to a text file
with open('askreddit_titles.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        f.write(title + '\n')

print("Titles extracted and saved to askreddit_titles.txt")
