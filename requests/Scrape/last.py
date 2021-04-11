import requests
import os
import json
from requests_oauthlib import OAuth1
from auth import *
from datetime import date, timedelta
import time
import sys

#SET URL AND AUTH
url = 'https://api.twitter.com/1.1/tweets/search/fullarchive/epitechdigital.json'
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

#GET IMPORTANT GLOBAL VAR
q = input("Query: ")
year = input("From: ")

#SET GLOBAL VARS
all_id = {}
nb_q = 0
nb_t = 0
theapi = {}
q_array_mrg = {}
#DELETE PREVIOUS QUERIES FROM Q



#SCRAPER
def alldays(year):
    dates = date(year, 1, 1)
    alldates = []
    while dates.year < year+1:
        alldates.append(dates)
        dates += timedelta(days = 7)
    return alldates

the_date = alldays(int(year))
for i in range(1):
    from_date = the_date[i]
    from_date = str(from_date).replace('-', '')
    to_date = the_date[i+1]
    to_date = str(to_date).replace('-', '')
    querys = requests.get(url, params={'query': q,' maxResults': 2, 'fromDate': from_date + '0000', 'toDate': to_date + '0000'}, auth=auth)
    f = open( 'birth' + '.json', 'a')
    f.write(querys.text)
    f.close
    """json_query = querys.json()['results']
    count_json = len(json_query)
    nb_q += count_json"""
    for remaining in range(2, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)

#ANSWER
"""print('La requête a permis de récolter ' + str(nb_q) + ' tweets')"""