import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2019645066:AAFw5qEU_JI16Dq_IOs4N40e4sqrhGoMe_A")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 1468557))
    API_HASH = os.environ.get("API_HASH", "c05a1fff8d688c198d4665f4c08016a2")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1268206396 746022062").split())

    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "postgres://gqablzuxxhgibu:fabd3cc46bb3ef472017b3bbea20446be3c79df6bd425b76f114cd85397222bd@ec2-176-34-116-203.eu-west-1.compute.amazonaws.com:5432/dafle5puaqafqi"
