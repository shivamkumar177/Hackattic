import requests
import base64

def main():
    #get the bytes
    bytes_data = requests.get("https://hackattic.com/challenges/help_me_unpack/problem?access_token=89e09ce7719984fb")
    bytes_data = bytes_data.json()
    

if __name__ == "__main__":
    main()