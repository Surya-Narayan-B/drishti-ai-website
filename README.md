# DrishtiAI - Your Personal Wellness Dashboard

DrishtiAI is an intelligent, real-time wellness monitor designed to help you build healthier screen habits. Using your webcam, it tracks key indicators of visual and mental fatigue, providing smart alerts and a conversational AI assistant to guide you toward a more balanced workday.

**[Live Demo URL Will Go Here]**

---

## ✨ Key Features

* **Intelligent Fatigue Score:** Instead of simple alerts, DrishtiAI calculates a unified fatigue score based on a pattern of behaviors, including long blinks, head nods, and yawns, for more accurate drowsiness detection.
* **Advanced Gaze & Head Pose Tracking:** A robust 2.5D head pose model accurately tracks your gaze direction and distinguishes between drowsy head nods and simple posture changes like leaning back.
* **Real-Time Monitoring:** A live dashboard visualizes your blink rate (BPM), active time, and fatigue score, giving you immediate feedback on your screen habits.
* **Conversational AI Assistant:** Powered by Google Gemini, the AI assistant remembers your conversation and can provide wellness tips, explain your stats, or answer general questions.
* **Personalized Calibration:** A one-time calibration process tunes the detection parameters to your unique facial structure and environment, ensuring high accuracy.
* **Smart Alerts & Reminders:** The application provides notifications for eye strain (staring), low blink rates, and scheduled breaks based on the 20-20-20 rule.

---

## 💻 Technology Stack

* **Backend:** Python, Flask, OpenCV, MediaPipe
* **AI:** Google Gemini
* **Frontend:** Astro, JavaScript, Chart.js
* **Database:** SQLite

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* A webcam

### Installation & Setup

1.  **Clone the repositories:**
    ```bash
    # Clone the backend
    git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/<YOUR_BACKEND_REPO>.git
    # Clone the frontend
    git clone [https://github.com/Surya-Narayan-B/drishti-ai-website.git](https://github.com/Surya-Narayan-B/drishti-ai-website.git)
    ```
2.  **Setup the Backend:**
    ```bash
    cd <YOUR_BACKEND_REPO>
    pip install -r requirements.txt
    python real_time_eye_tracking.py
    ```
3.  **Setup the Frontend:**
    ```bash
    cd ../drishti-ai-website
    npm install
    npm run dev
    ```
4.  Open your browser to `http://localhost:4321` to view the application.

---

## 🔮 Future Improvements

* Create a standalone `.exe` file for easy distribution using PyInstaller.
* Enhance session reports with more detailed visualizations.

---

Created by [Surya Narayan].