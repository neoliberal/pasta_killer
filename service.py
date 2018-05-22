"""service file"""
import os
import praw

try:
    from pastakiller import PastaKiller
except ModuleNotFoundError:
    from .pastakiller import PastaKiller

def main():
    """main service function"""
    reddit = praw.Reddit(
        client_id=os.environ["pastakiller_client_id"],
        client_secret=os.environ["pastakiller_client_secret"],
        refresh_token=os.environ["pastakiller_refresh_token"],
        user_agent=os.environ["pastakiller_user_agent"]
    )

    bot = PastaKiller(
        reddit,
        os.environ["pastakiller_subreddit"],
        minimum_length = int(os.environ["pastakiller_minlen"]),
        match_threshold = int(os.environ["pastakiller_matchthreshold"]),
        mods = os.environ["pastakiller_mods"].split(","),
        ignored_strings = os.environ["pastakiller_ignored_strings"].split(",")
    )

    while True:
        bot.kill()

    return

if __name__ == "__main__":
    main()
