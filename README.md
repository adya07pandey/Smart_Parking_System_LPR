Got it! Here’s a **beautified version** of the README with clear, attractive headings and consistent formatting.

---

# 🚗 **Smart Parking System with License Plate Recognition**

---

## 📂 **Repository Structure**

```
Smart_Parking_System_LPR/
├── parking_system.py             # 🚧 Core parking logic: barriers, sensors, LCD
├── license_plate_recognition.py  # 🔍 License Plate Recognition with OpenCV & OCR APIs
├── README.md                     # 📘 Project documentation
```

---

## 🎯 **Project Overview**

This is an **IoT-based Automated Smart Parking System** using a **Raspberry Pi**, combining:

* 🚘 **Vehicle Detection:** Ultrasonic sensors for entry, exit & slots.
* 🔐 **Barrier Automation:** Servo motors for gate control.
* 📺 **Live Display:** Real-time slot info & fee on an I2C LCD.
* 🔍 **LPR Module:** License Plate Recognition using **OpenCV**, **pytesseract**, and the **OCR.Space API**.

---

## ✨ **Features**

✅ Automated vehicle entry & exit detection
✅ Barrier control with servos
✅ Real-time available slot count
✅ Parking fee calculation based on stay duration
✅ Camera feed for plate capture
✅ Dual OCR methods: Local (`pytesseract`) & Cloud (`OCR.Space`)

---

## ⚙️ **Requirements**

**🔌 Hardware:**

* Raspberry Pi (GPIO support)
* Ultrasonic sensors (HC-SR04)
* Servo motors (entry & exit barriers)
* I2C 16x2 LCD Display
* Camera (USB or IP, e.g., DroidCam)

**💻 Software:**

* Python 3.x
* `opencv-python`
* `pytesseract`
* `smbus2`
* `RPLCD`
* `requests`
* `Pillow (PIL)`

---

## 🚀 **Setup & Run**

1️⃣ **Install dependencies:**

```bash
pip install opencv-python pytesseract smbus2 RPLCD requests pillow
```

2️⃣ **Connect hardware:**

* Wire all sensors, servos & LCD as per GPIO pins in `parking_system.py`.

3️⃣ **Run the Parking System:**

```bash
python parking_system.py
```

4️⃣ **Run License Plate Recognition:**

```bash
python license_plate_recognition.py
```

> ✅ **Tip:** Ensure the IP in `droidcam_url` is your camera’s correct IP.

---

## 🔄 **How It Works**

* 🚗 **Entry:** Vehicle detected → barrier opens → parking time logged → slot count updates.
* 🚪 **Exit:** Vehicle detected → fee calculated → barrier opens → slot freed.
* 🖥️ **Display:** LCD shows slots left & fee.
* 📸 **LPR:** Camera captures frames, extracts text with OCR, prints plate numbers.

---

## ⚠️ **Cleanup & Safety**

* On `KeyboardInterrupt` (`Ctrl+C`):

  * Servo PWM stops.
  * GPIO pins are cleaned up.
  * LCD display is cleared.

---

## 🔑 **Notes**

* Replace the **API key** in `license_plate_recognition.py` with your own if needed: [OCR.Space](https://ocr.space/).
* Tune ultrasonic thresholds based on your sensor range.
* For best LPR accuracy, ensure good lighting & camera focus.

---

## 👥 **Team**

Built by **\[Your Team Name]**
📫 *Add your contact info here if you’d like!*

---

## 📜 **License**

This project is for **educational use** — feel free to adapt and improve it!

---

If you’d like, I can package this as a ready `README.md` file for you. Just say **“Yes, save it for me”**!
