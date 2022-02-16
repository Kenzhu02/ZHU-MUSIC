from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME","KenzuXMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999999999999"))
SESSION_NAME = getenv("SESSION_NAME")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! ").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2014359828 1641370961").split()))
