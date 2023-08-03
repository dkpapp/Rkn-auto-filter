import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Request Channels
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', '-1001818554544'))


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID','26382274'))
API_HASH = environ.get('API_HASH', '19eb49cac0c8f886b9a45b32b27c237a')
BOT_TOKEN = environ.get('BOT_TOKEN', "6019972009:AAEAfErAbjFpJnwFfII5K1oPikw0kSR7zH0")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://telegra.ph/file/b806ad314d0c415571bde.jpg https://graph.org/file/fc80c462657261a1b6e3f.jpg')).split()
#PIC = (environ.get('PICS' ,'https://telegra.ph/file/f9ff43ac9a72c4dfd75c1.jpg https://telegra.ph/file/f6da7741e57daac351a8b.jpg https://telegra.ph/file/c51248450e539480953ce.jpg https://telegra.ph/file/98842f9fe8978a8688b9c.jpg https://telegra.ph/file/139e874011a7f6175c3ef.jpg https://telegra.ph/file/9f4137c00d4daac7bb5fd.jpg https://telegra.ph/file/5915c9a73683189e8aafb.jpg https://telegra.ph/file/643ff05841fae4e1519a7.jpg https://telegra.ph/file/31fa390308ef95aa6f198.jpg https://telegra.ph/file/643ff05841fae4e1519a7.jpg https://telegra.ph/file/98842f9fe8978a8688b9c.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2067727305', '2103555754').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '2067727305').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001957984770')
auth_grp = environ.get('AUTH_GROUP', '-1001517645234')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://480p:encode@cluster0.7fgwrif.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '👋 𝙷𝙴𝙻𝙾 {user}\n\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {bot},\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽...')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒐 𝑼𝒔𝒆 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕!')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hai {user}\nwelcome to {chat}")
PMFILTER = environ.get('PMFILTER', "True")
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = environ.get("BUTTON_LOCK", "True")

# url shortner
SHORT_URL = environ.get("SHORT_URL", "shareus.io")
SHORT_API = environ.get("SHORT_API", "TLRBhlLOb7TPKsbsBbngMIS0pu43")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "86000"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001818554544'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Mannu_Production')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
PM_IMDB = environ.get('PM_IMDB', "True")
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "Hey {mention}👋\n\n{file_name}\n\n🔘 size - {file_size}\n\n╭─── • ❰ @MS_Dhaliwal ❱ • ────➤\n┣ ▫️ @Mannu_Production\n┣ ▫️ SHARE AND SUPPORT\n╰─────── • ◆ • ───────➤")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10\n<b>☀️ Languages</b> : <code>{languages}</code>\n<b>👨‍💼 Dɪʀᴇᴄᴛᴏʀ</b>: {director}\n<b>👨🏻‍🦱 Pʀᴏᴅᴜᴄᴇʀ</b>: {producer}\n<b>📑 wʀɪᴛᴇʀ</b>: {writer}\n<b>📀 RunTime</b>: {runtime} Minutes\n<b>📆 Release Info</b> : {release_date}\n<b>🎛 Countries</b> : <code>{countries}</code>\n<b>📓 Sᴛᴏʀy</b> : <code>{plot}</code>\n\n\n<b>🍀Requested by🍀</b> : {message.from_user.mention}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('-1001818554544', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#request force sub
REQ_SUB = bool(environ.get("REQ_SUB", True))
SESSION_STRING = environ.get("SESSION_STRING", "")
