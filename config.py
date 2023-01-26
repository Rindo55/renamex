import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "5426835246:AAGpWNE1EQF5_t56BmcdD8QWSJhCtynh3gk"
    # The Telegram API things
    APP_ID = "3845818"
    API_HASH = "95937bcf6bc0938f263fc7ad96959c6d"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = "-1001730306649"
    # log channel
    #LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
    # Get these values from my.telegram.org
    CHAT_ID = "-1001526605992"
    # Array to store users who are authorized to use the bot
    AUTH_USERS = "1443454117"
    # Banned Unwanted Members..
    BANNED_USERS = []
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "")
    
