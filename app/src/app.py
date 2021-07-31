# -*- coding: utf-8 -*-
import httplib2
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
sys.path.append('./')
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

CLIENT_SECRETS_FILE = PYTHON_APP_HOME + '/config/client_secret.json'
OAUTH_FILE = PYTHON_APP_HOME + '/config/app.py-oauth2.json'

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

VIDEO_ID = "L-oNKK1CrnU"

def get_authenticated_service(oauth_file):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    scope=YOUTUBE_READ_WRITE_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage(oauth_file)
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    flags = argparser.parse_args()
    credentials = run_flow(flow, storage, flags)

  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))

def like_video(youtube, video_id):
  youtube.videos().rate(
    id=video_id,
    rating="like"
  ).execute()

if __name__ == '__main__':
  logger.info('Start')

  youtube = get_authenticated_service(OAUTH_FILE)
  like_video(youtube, VIDEO_ID)

  logger.info('Finish')
