# reddit-saved-to-csv
Exports saved posts and comments on Reddit to a csv file.

**Columns**: ID, Name, Subreddit, Type, URL, NoSFW
- ID: Starts from 1 and increments for each saved Post or Comment.
- Name: Title of the post.
- Subreddit: Display name of the subreddit.
- Type: Either #Comment or #Post.
- URL: Link of the comment or the post.
- NoSFW: True or False based on the post.

## How to Use
* Download or clone the code to your pc.
* Install [Python3](https://www.python.org/downloads/) and then install [praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html).
* Go to https://www.reddit.com/prefs/apps and create a script.
  * Give any name and description.
  * Redirect uri: http://localhost:8080
  * Create
  * Text below "personal use script" is your client id. We'll need that and the secret.
* Open `reddit_saved_to_csv.py` file with any text editor.
* You'll see below lines at the top:
```python
client_id='' # Enter your client ID
client_secret='' # Enter you client secret
username='' # Enter Username
password='' # Enter password
```
* Enter the necessary information into the quotation marks.
* Save the .py file.
* Now you can run the script through command line/ VSCode/ Spyder etc.
* Wait until you get the "**COMPLETED!**" message.
