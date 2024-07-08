import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7371147227:AAH6X5SQgkXrlpLxO48-trcjp81pOEJk0Tk")
    API_ID = int(os.environ.get("API_ID", "21211387"))
    API_HASH = os.environ.get("API_HASH", "82767b47d8c3d45a00fcf29cdbc7729f")
    CHANNEL = os.environ.get("CHANNEL", "@jawfe")
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
