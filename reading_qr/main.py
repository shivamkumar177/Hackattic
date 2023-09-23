import cv2
import requests, json
from PIL import Image
import io
import numpy as np 
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

if __name__ == "__main__":
    image = (requests.get(f"https://hackattic.com/challenges/reading_qr/problem?access_token={ACCESS_TOKEN}").json())['image_url']
    qr_data = requests.get(image)
    # open cv image
    image_pil = Image.open(io.BytesIO(qr_data.content))
    image_np = np.array(image_pil)
    qr_decoder = cv2.QRCodeDetector()
    data, bbox, newImage = qr_decoder.detectAndDecode(image_np)
    if len(data) > 0:
        print(data)
        payload = json.dumps({"code":data})
        resp = requests.post(f"https://hackattic.com/challenges/reading_qr/solve?access_token={ACCESS_TOKEN}", data=payload)
        print(resp.json())
    else:
        print("No QR Code detected")


