import cv2
import time
import requests
import pytesseract
from PIL import Image

API_KEY = "helloworld"  # Free tier API key

def ext_txt(img_pth):
    with open(img_pth, "rb") as image_file:
        payload = {
            "apikey": API_KEY,
            "language": "eng",
            "isOverlayRequired": False
        }
        files = {"file": image_file}
        response = requests.post("https://api.ocr.space/parse/image", files=files, data=payload)
        
        try:
            result = response.json()
        except ValueError:
            print("❌ Failed to parse JSON response")
            print("Response content:", response.text)
            return
        
    if isinstance(result, dict) and "ParsedResults" in result:
        text = result["ParsedResults"][0].get("ParsedText", "")
        print("📝 OCR Output:", text)
    else:
        print("❌ OCR failed or no text found")
        print("Full Response:", result)

def pytsr(img_pth):
    text = pytesseract.image_to_string(Image.open(img_pth), lang="eng")
    print("📝 OCR Output:", text)
    

print(cv2._version_)

droidcam_url = "http://192.168.137.175:4747/video"
cap = cv2.VideoCapture(droidcam_url)

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

capture_interval = 10  # seconds
last_capture_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    current_time = time.time()
    if current_time - last_capture_time >= capture_interval:
        image_filename = f"capture_{int(current_time)}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Image saved: {image_filename}")
        last_capture_time = current_time
        pytsr(image_filename)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
