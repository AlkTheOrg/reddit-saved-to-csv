#!python3
# reddit_saved_to_csv.py - Exports your saved Posts and Comments on Reddit to a csv file.

import argparse
import csv
import codecs
import praw

# Argparse
parser = argparse.ArgumentParser(description='Exports your saved posts and comments on Reddit to a csv file.')

parser.add_argument('-u', '--username', help='Username of the Reddit account.', required=True)
parser.add_argument('-p', '--password', help='Password of the Reddit account.', required=True)
parser.add_argument('-id', '--client_id', help='Reddit Client ID', required=True)
parser.add_argument('-s', '--client_secret', help='Reddit Client Secret', required=True)
parser.add_argument('-f', '--file', help='Name of the csv file to be created.', default='reddit_saved.csv')

# Post limits
parser.add_argument('-l', '--limit', help='Number of posts to be exported.', default=None)

args = parser.parse_args()

# Get arguments
reddit = praw.Reddit(client_id=args.client_id,
                     client_secret=args.client_secret,
                     user_agent=f'Saved posts scraper by /u/{args.username}',
                     username=args.username,
                     password=args.password)

reddit_home_url = 'https://www.reddit.com'

# models: Comment, Submission
saved_models = reddit.user.me().saved(limit=args.limit)

# creating our csv file
reddit_saved_csv = codecs.open(args.file, 'w', 'utf-8')

# CSV writer for better formatting
saved_csv_writer = csv.writer(reddit_saved_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Write column names
saved_csv_writer.writerow(['ID', 'Name', 'Subreddit', 'Type', 'URL', 'NoSFW'])

def handle(saved_models):
    count = 1
    for model in saved_models:
        subreddit = model.subreddit # Subreddit model that the Comment/Submission belongs to
        subr_name = subreddit.display_name
        url = reddit_home_url + model.permalink

        if isinstance(model, praw.models.Submission): # if the model is a Submission
            title = model.title
            noSfw = str(model.over_18)
            model_type = '#Post'
        else: # if the model is a Comment
            title = model.submission.title
            noSfw = str(model.submission.over_18)
            model_type = '#Comment'

        # Write to csv file
        saved_csv_writer.writerow([str(count), title, subr_name, model_type, url, noSfw])

        # Print update
        print(f'Saved {count}/{len(saved_models)} - {title}')

        count += 1

handle(saved_models)
reddit_saved_csv.close()

print('\nCOMPLETED!')
print(f'Your saved posts are available in {args.file} file.')

