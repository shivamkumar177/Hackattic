import cv2
import requests, json
from PIL import Image
import io
import numpy as np 

if __name__ == "__main__":
    image = (requests.get("https://hackattic.com/challenges/reading_qr/problem?access_token=89e09ce7719984fb").json())['image_url']
    qr_data = requests.get(image)
    # open cv image
    image_pil = Image.open(io.BytesIO(qr_data.content))
    image_np = np.array(image_pil)
    qr_decoder = cv2.QRCodeDetector()
    data, bbox, newImage = qr_decoder.detectAndDecode(image_np)
    if len(data) > 0:
        print(data)
        payload = json.dumps({"code":data})
        resp = requests.post("https://hackattic.com/challenges/reading_qr/solve?access_token=89e09ce7719984fb", data=payload)
        print(resp.json())
    else:
        print("No QR Code detected")


