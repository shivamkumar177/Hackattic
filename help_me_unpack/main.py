import json
from struct import unpack
import requests
import base64

def maybe(Ex):
    print(Ex)

def main():
    #get the bytes
    bytes_data = requests.get("https://hackattic.com/challenges/help_me_unpack/problem?access_token=89e09ce7719984fb")
    bytes_data = bytes_data.json()['bytes']
    bytes_data = (base64.b64decode(bytes_data))
    data = json.dumps({
        'int': unpack("<i", bytes_data[:4])[0],
        'uint': unpack("<I", bytes_data[4:8])[0],
        'short': unpack("<h", bytes_data[8:10])[0],
        "float": unpack("<f", bytes_data[12:16])[0],
        "double": unpack("<d", bytes_data[16:24])[0],
        "big_endian_double": unpack(">d", bytes_data[24:32])[0]
    })
    resp = requests.post('https://hackattic.com/challenges/help_me_unpack/solve?access_token=89e09ce7719984fb', data= data)
    print(resp.json())
    

if __name__ == "__main__":
    main()