import base64
import json
import traceback
import requests
import os
import subprocess
from dotenv import load_dotenv
from db import DbPostgres

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')


def submit_answer(data):
    resp = requests.post(f'https://hackattic.com/challenges/backup_restore/solve?access_token={ACCESS_TOKEN}', data=json.dumps(data)).json()
    print(resp)

try:
    probelem_data = requests.get(f'https://hackattic.com/challenges/backup_restore/problem?access_token={ACCESS_TOKEN}').json()['dump']
    probelem_data_bytes = base64.b64decode(probelem_data)
    with open('backup_restore/pg_dump.dump','wb') as f:
        f.write(probelem_data_bytes)
        f.close()
    # copy file in docker and dump data
    copy_file_command = f"docker cp /Users/shivamkumar/Developer/Hackattic/backup_restore/pg_dump.dump postgresdb2:/tmp/"
    subprocess.run(copy_file_command, shell=True)
    # uncompress and dump
    dump_command = f'docker exec -i postgresdb2 /bin/bash -c "gunzip -c /tmp/pg_dump.dump | psql -U {DB_USER} -d {DB_NAME}"'
    subprocess.run(dump_command, shell=True)

except Exception as e:
    print(e)
    print(traceback.format_exc())  
# run twice first while getting data and once while submitting answer
# load the dump file to postgres server 
# used postgres on docker 
# docker run --name postgresdb -e POSTGRES_PASSWORD=**** -d postgres
# create database 
# load file via copying into docker container
# gunzip -c /tmp/pg_dump.dump | psql -U postgres -d demo_hackattic

# could have used subprocess libaray to do it via script

# it has timelimit this approach fails

# DID IT 

try:

    ssn_list = []
    # db cnnection
    db = DbPostgres(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD)
    db.connect()
    query = "SELECT ssn from criminal_records where status = 'alive'"
    results = db.execute_query(query)
    db.close()
    for row in results:
        ssn_list.append(row[0])
    data = {
        "alive_ssns": ssn_list
    }
    submit_answer(data)
    print(ssn_list)
    print(len(ssn_list))
except Exception as e:
    print(e)
    print(traceback.format_exc())
