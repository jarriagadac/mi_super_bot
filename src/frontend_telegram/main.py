from include.telegram import bot_start

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

if __name__ == "__main__":
    bot_start()
