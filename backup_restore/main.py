import base64
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# probelem_data = requests.get(f'https://hackattic.com/challenges/backup_restore/problem?access_token={ACCESS_TOKEN}').json()['dump']
# probelem_data_bytes = base64.b64decode(probelem_data)
# with open('backup_restore/pg_dump.dump','wb') as f:
#     f.write(probelem_data_bytes)
#     f.close()
# run twice first while getting data and once while submitting answer
# load the dump file to postgres server 
# used postgres on docker 
# docker run --name postgresdb -e POSTGRES_PASSWORD=**** -d postgres
# create database 
# load file via copying into docker container
# gunzip -c /tmp/pg_dump.dump | psql -U postgres -d demo_hackattic

# could have used subprocess libaray to do it via script

# it has timelimit this approach fails


ssn_list = []

with open('backup_restore/output.txt','r') as f:
    for line in f:
        ssn = line.strip()
        if ssn:
            if (ssn[0].isnumeric()):
                ssn_list.append(ssn)


data = {
    "alive_ssns": ssn_list
}
resp = requests.post(f'https://hackattic.com/challenges/backup_restore/solve?access_token={ACCESS_TOKEN}', data=json.dumps(data)).json()
print(resp)
print(ssn_list)
print(len(ssn_list))