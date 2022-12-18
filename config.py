from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN" ,"5947463448:AAGoOQ8GRiSH_NHDgrAcs4L-fvMcd0A-aVk")
API_ID = int(getenv("API_ID", "14739013"))
API_HASH = getenv("API_HASH" ,"0d4ffaf95ba8e5dac2c6df849d86213d")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1955509952").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1955509952").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001759657140"))
OWNER_USERNAME = str(getenv("OWNER_USERNAME" ,"cl_me_logesh"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME" ,"logi")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/dev-logesh/music-video-bot"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))

STRING_SESSION1="BQBD1fTjePi95vr0b0UhM2LYVlhOmFLETWqX3k9IKNKyewE12ptohui2NZxTozHHAVowsfBnzkW_p7NP67lYhG3ujyyLjchiyfEj5c4dKURctQkJThgibR_Lrc52CX5cIpK-sLDdsnwtO0Ppb8GpIoaMLEvf1kbuEBxqAFochWbcD3uR6UlPvp8DQgHSQ9W_Z_8_6nGwxGkNUv-7faKj0VrnVFRYA8sNnGGOJZPyIzx13_JqQvUb1lWn67PvT7HTteqAMqXuLgBSAewCJLuKF2crYqeCojJLv0JBU2n3MJCoRd6KWjp8mwboCqt0IG2H3fjNXZuNlvfx-OANszqOWEohAAAAAU0hUXYA"

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
