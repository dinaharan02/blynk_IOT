# IoT Dashboard (Django + Blynk Integration)

A real-time IoT dashboard built using **Django** that connects to Blynk Cloud APIs to display sensor data like temperature, humidity, and soil moisture.

---

## Features

* Real-time data fetching (AJAX polling)
* Device online/offline detection
* Temperature, Humidity, Soil monitoring
* Optimized parallel API requests
* Modern responsive UI
* Safe handling of offline/stale data

---

## Tech Stack

* Python (Django)
* HTML, CSS, JavaScript
* Requests library
* Blynk Cloud API

---

## Prerequisites

Make sure you have installed:

* Python 3.8+
* pip
* Virtualenv (optional but recommended)

---

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/iot-dashboard.git
cd iot-dashboard
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install django requests python-dotenv
```

---

## 4. Create `.env` File (IMPORTANT)

In the project root (same level as `manage.py`), create a file named:

```
.env
```

### Add your environment variables:

```env
BLYNK_TOKEN=your_blynk_auth_token_here
BASE_URL=https://blynk.cloud/external/api
```

---

## 5. Load `.env` in Django

### Install dotenv (if not already):

```bash
pip install python-dotenv
```

### Update `settings.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

BLYNK_TOKEN = os.getenv("BLYNK_TOKEN")
BASE_URL = os.getenv("BASE_URL")
```

---

## 6. Add `.env` to `.gitignore`

Create or update `.gitignore`:

```
.env
venv/
__pycache__/
```

 This prevents leaking your secret token.

---

## 7. Apply Migrations

```bash
python manage.py migrate
```

---

## 8. Run the Server

```bash
python manage.py runserver
```

---

## 9. Open in Browser

```
http://127.0.0.1:8000/
```

---

## Real-Time Data Flow

```
ESP32 → Blynk Cloud → Django API → HTML Dashboard
```

* Data updates every 2 seconds
* Automatically handles offline devices
* Prevents stale data display

---

## API Endpoints

| Endpoint         | Description            |
| ---------------- | ---------------------- |
| `/`              | Dashboard UI           |
| `/api/realtime/` | Fetch live sensor data |

---