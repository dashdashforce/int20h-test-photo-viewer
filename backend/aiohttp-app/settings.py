import logging
import os

from dotenv import find_dotenv, load_dotenv
from traitlets import Bool, Dict, Integer, Unicode

load_dotenv(find_dotenv())

DEBUG = Bool(
    os.getenv('DEBUG', default=False) == 'True',
    config=False,
    help='Debug mode'
)

PORT = Integer(
    int(os.getenv('PORT')), config=True,
    help='The port the server will listen on.'
)
ALLOW_ORIGIN = Unicode(
    '*', config=True,
    help="""Set the Access-Control-Allow-Origin header
        Use '*' to allow any origin to access your server.
        Takes precedence over allow_origin_pat.
        """
)

LOG_NAME = "PhotoViewerApp Log"


@property
def app_log():
    return logging.getLogger(log_name)
