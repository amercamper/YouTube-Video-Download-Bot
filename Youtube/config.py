import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("7371147227:AAH6X5SQgkXrlpLxO48-trcjp81pOEJk0Tk", "")
    API_ID = int(os.environ.get("21211387", ))
    API_HASH = os.environ.get("82767b47d8c3d45a00fcf29cdbc7729f", "")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("@jawfe", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
