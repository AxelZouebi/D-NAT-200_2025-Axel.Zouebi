import requests
import os
import json
from requests_oauthlib import OAuth1
from auth import *

#SET URL AND AUTH
url = 'https://api.twitter.com/1.1/search/tweets.json'
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

#GET IMPORTANT GLOBAL VAR
q = input("Query: ")
nb_r = input("Request's number: ")

#GET QUERY
query = requests.get(url, params={'q': q, 'count': 50}, auth=auth)

#SET VAR MAX & MIN
max_id = query.json()['search_metadata']['max_id'] + 2500000000000000
min_id = query.json()['search_metadata']['since_id']
max = max_id
min = min_id

#SET GLOBAL VARS
all_id = {}
nb_t = 0
theapi = {}
q_array_mrg = {}
#DELETE PREVIOUS QUERIES FROM Q

#SCRAPER
for i in range(int(nb_r)):
    querys = requests.get(url, params={'q': q, 'count': 50, 'since_id': min, 'max_id': max}, auth=auth)
    if 'statuses' not in querys.json():
        max = max + 2500000000000000
        min = min + 2500000000000000
    else:
        json_query = querys.json()['statuses']
        count_json = len(json_query)
        if count_json == 0:
            max = max + 2500000000000000
            min = min + 2500000000000000
        else:
            for n in range(count_json):
                ids = querys.json()['statuses'][n]['id']
                all_id[i] = ids
            if count_json > 0:
                if i == 0:
                    print(query.json()['search_metadata']['max_id'])
                    nb_t += count_json                        
                    for n in range(count_json):
                        querys.json()['statuses'][n]['id']
                        id = querys.json()['statuses'][n]['id']
                        text = querys.json()['statuses'][n]['text']
                        created_at = querys.json()['statuses'][n]['created_at']
                        q_array_mrg[n] = [{'id': id, 'text': text, 'created_at': created_at}]
                    theapi['query'+str(i)] = q_array_mrg
                else:
                    print(query.json()['search_metadata']['max_id'])
                    im = i - 1
                    is_equal = all_id[im] == all_id[i]
                    if is_equal == True:
                        max = max + 2500000000000000
                        min = min + 2500000000000000
                    else:
                        nb_t += count_json
                        for n in range(count_json):
                            id = querys.json()['statuses'][n]['id']
                            text = querys.json()['statuses'][n]['text']
                            created_at = querys.json()['statuses'][n]['created_at']
                            q_array_mrg[n] = [{'id': id, 'text': text, 'created_at': created_at}]
                        theapi['query'+str(i)] = q_array_mrg
                        max = max + 2500000000000000
                        min = min + 2500000000000000

directory = q
path_dir = r"C:\Users\axelz\OneDrive\Documents\Epitech Digital\Projet\Storks\Storks\resources\json"
if not os.path.exists(path_dir + "\\"+ q):
    os.mkdir(os.path.join(path_dir, q))
f = open(os.path.join(path_dir + "\\"+ q, q + '.json'), 'w')
total = json.dumps(theapi)
f.write(total)
f.close

#ANSWER
print('La requête a permis de récolter ' + str(nb_t) + ' tweets')