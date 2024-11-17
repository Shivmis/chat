from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "24946423"
# -------------------------------------------------------------
API_HASH = "30ba9fa7064625f3d952b8adb75f636c"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7491834397"))
BOT_ID = int(getenv("BOT_ID", "7799481163"))
SUPPORT_GRP = "FRIENDS_ZONE_GP"
UPDATE_CHNL = "shivang_xd"
OWNER_USERNAME = "shivang_mishra_op"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002465721301"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "8056154987").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Badhacker98/Chat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
