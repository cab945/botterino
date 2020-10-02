import praw
# See readme for instructions
client_secret = None
client_id = None
username = None
password = None
user_agent = None

roundfile = "rounds.yaml"
archivefile = "archive.yaml"

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password,
)

pg = reddit.subreddit('picturegame')

clarification = """ CLARIFICATION on coordinate format:

I want coordinates in either of the two formats given by google maps.

[Here](https://i.imgur.com/xGomrVp.png) is an example, either the top or the bottom format is acceptable.

The coordinates can appear anywhere in your commment, but they need to be in one of those two formats.

Please not that if you are using google earth, your coordinates will be given in a slightly different format

which will not be counted correct.
"""

donotreply = {
    'achievements-bot',
    username.lower(),
    'r-picturegame',
    'imreallycuriousbird',
}

incorrect = [
    "incorrect",
    "sorry, that's not the right answer",
    "that's not right but keep trying",
    "nope",
    "This isn't it. Maybe you should consider giving up.",
    "scusa, ma la risposta non è corretta. Se ritieni che ciò sia stato errato, contatta /u/getoofded",
    "This is not correct, but I belive in you. Never give up",
    "negative",
    "+incorrect",
    "if wrong answers were acceptable this would be correct",
    "❌",
    "🙅‍♂️",
    "👎",
    "I am not able to comprehend what could have led you to arrive at such an answer, ❌",
    "🤦‍♀️",
    "🤦‍♂️",
    "错",
    "間違っているが日本語で書かれている ❌",
    "no dice",
    "https://www.youtube.com/watch?v=wKjxFJfcrcA",
]

coords_not_found = """
If this is a guess, I was not able to find your coordinates.
Make sure you are using the correct coordinate format.
This action was performed automatically by a botterino.
Please contact /u/getoofded if you experience any issues
"""