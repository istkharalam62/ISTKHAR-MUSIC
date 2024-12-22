from ISTKHARMUSIC.core.bot import ISTKHAR
from ISTKHARMUSIC.core.dir import dirr
from ISTKHARMUSIC.core.git import git
from ISTKHARMUSIC.core.userbot import Userbot
from ISTKHARMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "InflexMusicRobot"  # connect music api key "Dont change it"