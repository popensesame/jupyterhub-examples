
import requests

api_url = 'http://127.0.0.1:8000/hub/api'
# Keep it secret, keep it safe
token = '2f9d88896b7cf390a4c3f1d0e8a813e4de563a87d33bd3fd3ad09a25d513295a'

r = requests.get(api_url + '/authorizations/token/' + token
