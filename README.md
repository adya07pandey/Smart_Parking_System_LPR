Here’s a clear and well-structured **README.md** for your team repository **Smart\_Parking\_System\_LPR** based on the code you provided:

---

## 📌 Smart\_Parking\_System\_LPR

An IoT-based fully automated Smart Parking System with **License Plate Recognition (LPR)** and **Dynamic Slot Management**, designed for Raspberry Pi integration.

---

## 📂 Repository Structure

```
Smart_Parking_System_LPR/
├── parking_system.py             # Core parking system logic: entry/exit barriers, slot counting, LCD display
├── license_plate_recognition.py  # License Plate Recognition using OpenCV, Tesseract, OCR.Space API
├── README.md                     # Project documentation
```

---

## 🚗 Project Overview

This system automates vehicle entry/exit using:

* **Ultrasonic Sensors** to detect vehicle presence at entry, exit, and parking slots.
* **Servo Motors** to control entry/exit barriers.
* **LCD Display** to show available slots and parking fee.
* **License Plate Recognition (LPR)** for capturing license plates via camera feed using **OpenCV** and **OCR APIs**.

---

## 🔧 Features

✅ Detect vehicle presence using ultrasonic sensors
✅ Open/close barriers automatically via servo motors
✅ Display available slots and fee on an I2C LCD
✅ Capture license plates using DroidCam or USB camera
✅ Extract plate text using `pytesseract` or **OCR.Space** API
✅ Basic parking fee calculation based on time parked

---

## 📌 Requirements

**Hardware:**

* Raspberry Pi (with GPIO support)
* Ultrasonic distance sensors (HC-SR04 or similar)
* Servo motors for entry and exit gates
* I2C LCD Display (16x2)
* Camera (USB or IP camera, e.g., DroidCam)

**Software:**

* Python 3.x
* OpenCV (`cv2`)
* pytesseract
* smbus2
* RPLCD
* requests
* PIL (Pillow)

---

## ⚙️ Setup & Run

1. **Install Dependencies:**

   ```bash
   pip install opencv-python pytesseract smbus2 RPLCD requests pillow
   ```

2. **Connect Hardware:**

   * Wire ultrasonic sensors to specified GPIO pins.
   * Connect servo motors to GPIO pins for barriers.
   * Attach I2C LCD and test connectivity.

3. **Run Parking System Logic:**

   ```bash
   python parking_system.py
   ```

4. **Run License Plate Recognition:**

   ```bash
   python license_plate_recognition.py
   ```

   > Make sure the IP address in `droidcam_url` matches your camera stream.

---

## ⚡ How It Works

* The **entry sensor** detects a vehicle → barrier opens → vehicle enters → parking time is stored.
* When leaving, the **exit sensor** detects a vehicle → parking fee is calculated → barrier opens.
* The LCD shows available slots and exit fee.
* `license_plate_recognition.py` runs in parallel to capture images from the camera feed every few seconds and extracts the plate number.

---

## 🛡️ Safety & Cleanup

On exit (`Ctrl+C`):

* All GPIO pins are cleaned up.
* PWM signals for servos are stopped.
* LCD is cleared.

---

## 🏷️ Note

* **API\_KEY** in `license_plate_recognition.py` uses the free tier of [OCR.Space](https://ocr.space/). Replace with your own key if needed.
* Adjust ultrasonic detection thresholds as per your sensor range and mounting.
* This is a basic prototype; LPR results can be improved with better image quality and lighting.

---

## 🤝 Team

Developed by \[Your Team Name]
**Project:** Smart\_Parking\_System\_LPR
**Contact:** \[Add email or contact details if needed]

---

## 📜 License

This project is for educational purposes only. Adapt, improve, and extend as needed!

---

If you’d like, I can generate this as a ready-to-use `README.md` file for you — just say **"Yes, generate it"** and I’ll attach it!
