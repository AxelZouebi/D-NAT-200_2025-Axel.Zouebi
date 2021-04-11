import requests
import os
import json
from requests_oauthlib import OAuth1
from auth import *

"""def json_dumps(args):
    for arg in range(args):
        arg = """
from datetime import date, timedelta
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
def allsundays(year):
    d = date(year, 1, 1)                    # January 1st
    d += timedelta(days = 7 - d.weekday())  # First Sunday
    while d.year < year+1:
        yield d
        d += timedelta(days = 7)
 
def re(d):
    for i in range(2):
        querys = requests.get(url, params={'q': q, 'count': 50, 'until': d}, auth=auth)
        if 'statuses' not in querys.json():
            f = open( q + 'dbg.json', 'a')
            f.write(str(d) + ' re2.2 - ' + str(query.json()['search_metadata']['max_id']) + "\n")
            f.close
            break
        else:
            json_query = querys.json()['statuses']
            count_json = len(json_query)
            if count_json == 0:
                f = open( q + 'dbg.json', 'a')
                f.write(str(d) + ' re2.2 - ' + str(query.json()['search_metadata']['max_id']) + "\n")
                f.close
                break
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
                            f = open( q + 'dbg.json', 'a')
                            f.write(str(d) + ' re2.2 - ' + str(query.json()['search_metadata']['max_id']) + "\n")
                            f.close
                            break
                        else:
                            nb_t += count_json
                            for n in range(count_json):
                                id = querys.json()['statuses'][n]['id']
                                text = querys.json()['statuses'][n]['text']
                                created_at = querys.json()['statuses'][n]['created_at']
                                q_array_mrg[n] = [{'id': id, 'text': text, 'created_at': created_at}]
                            theapi['query'+str(i)] = q_array_mrg

#SET URL AND AUTH
url = 'https://api.twitter.com/1.1/tweets/search/fullarchive/epitech.json'
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

#GET IMPORTANT GLOBAL VAR
q = input("Query: ")
year = input("Year: ")

#GET QUERY
query = requests.get(url, params={'q': q, 'count': 50}, auth=auth)

#SET VAR MAX & MIN
"""max_id = query.json()['search_metadata']['max_id'] + 2500000000000000
min_id = query.json()['search_metadata']['since_id']"""
max = 0 #max_id
min = 0 #min_id

#SET GLOBAL VARS
all_id = {}
nb_t = 0
theapi = {}
q_array_mrg = {}
#DELETE PREVIOUS QUERIES FROM Q

#SCRAPER
for d in allsundays(int(year)):
    
    querys = requests.get(url, params={'query': q, 'maxResults': 100}, auth=auth)
    f = open( q + '.json', 'w')
    f.write(querys.text)
    f.close
    if 'statuses' not in querys.json():
        f = open( q + 'dbg.json', 'a')
        f.write(str(d) + ' re2.2 - ' + str(query.json()['search_metadata']['max_id']) + "\n")
        f.close       
        re(d)
    else:
        json_query = querys.json()['statuses']
        count_json = len(json_query)
        if count_json == 0:
            f = open( q + 'dbg.json', 'a')
            f.write(str(d) + ' re2.2 - ' + str(query.json()['search_metadata']['max_id']) + "\n")
            f.close           
            re(d)
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
                        f = open( q + 'dbg.json', 'a')
                        f.write(str(d) + ' re2.2 - ' + str(query.json()['search_metadata']['max_id']) + "\n")
                        f.close
                        re(d)
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
print('La requête a permis de récolter ' + str(nb_t) + ' tweets') + "\n"