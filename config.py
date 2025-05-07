import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7545544173:AAFLyGXW3shlfcxDfd5CZ9X4JTBjlXkAGqs")
      API_ID = int(os.environ.get("APP_ID", 26649585))
      API_HASH = os.environ.get("API_HASH", "588a3ea6fd01ae88bd2e10fed7d55b2c")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "RahatMx")
