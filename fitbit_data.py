import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
import csv

access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1JTTE0iLCJzdWIiOiJCWUZNQjciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJlY2cgcnNldCByb3h5IHJwcm8gcm51dCByc2xlIHJjZiByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNzEwMTIzMjg3LCJpYXQiOjE3MTAwOTQ0ODd9.UNS8qrQvzrWsVl2CgtSrSTEjKV3xiNUhP2c44wIhPXM'
user_id = 'BYFMB7'

heart_rate_request = requests.get('https://api.fitbit.com/1/user/'+user_id+'/activities/heart/date/2024-03-01/1d/1min.json',
                                headers={'Authorization': 'Bearer ' + access_token})

print(heart_rate_request.status_code)
pprint(heart_rate_request.json()['activities-heart'])
