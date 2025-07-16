import cv2
import time
import requests
import pytesseract
import sqlite3
from datetime import datetime
from PIL import Image
from fuzzywuzzy import process, fuzz  # Install using: pip install fuzzywuzzy python-Levenshtein

API_KEY = "helloworld"
DB_NAME = "license_plates.db"

# Allowed license plates
ALLOWED_PLATES = {"MP07TN4000", "ND13UX3741", "HJ64MP3100"}

def init_db():
    """Initialize the SQLite database and create table if not exists."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS plates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plate_text TEXT NOT NULL,
                entry_time TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except Exception:
        pass  # Ignore errors for smooth execution

def store_plate(plate_text):
    """Find the closest match and store it in the database if similar enough."""
    best_match, score = process.extractOne(plate_text, ALLOWED_PLATES, scorer=fuzz.ratio)
    if score >= 80:  # Accept matches with 80% similarity or more
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO plates (plate_text, entry_time) VALUES (?, ?)", (best_match, entry_time))
            conn.commit()
            conn.close()
        except Exception:
            pass  # Ignore errors

def extract_text_from_image(img_pth):
    """Extract text from an image using Tesseract OCR."""
    try:
        text = pytesseract.image_to_string(Image.open(img_pth), lang="eng").strip().replace(" ", "")
        if text:
            store_plate(text)
    except Exception:
        pass  # Ignore errors

def run_license_plate_recognition():
    """Runs the full license plate recognition process using DroidCam."""
    init_db()  # Initialize database

    droidcam_url = "http://192.168.137.175:4747/video"
    cap = cv2.VideoCapture(droidcam_url)

    if not cap.isOpened():
        return  # Stop if the camera is not accessible

    capture_interval = 10  # Capture every 10 seconds
    last_capture_time = time.time()

    while True:
        try:
            ret, frame = cap.read()
            if not ret:
                continue  # Skip if frame is not captured

            current_time = time.time()
            if current_time - last_capture_time >= capture_interval:
                image_filename = f"capture_{int(current_time)}.jpg"
                cv2.imwrite(image_filename, frame)
                extract_text_from_image(image_filename)
                last_capture_time = current_time

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # Stop if 'q' is pressed

        except Exception:
            pass  # Ignore unexpected errors

    cap.release()

# Call this function to start the process
run_license_plate_recognition()
