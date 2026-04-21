# 🛡️ SmartShield-AI: AI Engine Server

The **AI Engine Server** is the high-performance intelligent backend of the SmartShield-AI ecosystem. It provides a robust API for static file analysis and real-time behavioral malware detection, leveraging machine learning to identify both known threats and zero-day exploits.



## 🚀 Key Features

* **High-Performance API:** Built with **FastAPI** for asynchronous, high-concurrency request handling.
* **Static Analysis Engine:** Deep inspection of PE (Portable Executable) files using `pefile` to extract 23 critical structural features.
* **Hardware-Adaptive Inference:**
    * **High-Spec:** GPU/CUDA-accelerated inference for complex Neural Networks.
    * **Low-Spec:** Optimized CPU-bound inference for XGBoost/Random Forest models.
* **Continuous Learning Loop:** Dedicated endpoints for feedback-driven retraining, allowing the model to improve based on user-reported False Negatives.

## 🛠️ Tech Stack

* **Backend:** FastAPI, Uvicorn
* **Analysis:** `pefile` (Static), Sysmon (Behavioral log parsing)
* **Machine Learning:** XGBoost, Scikit-learn
* **Deployment:** Docker-ready, Gunicorn workers

---

## 🏗️ Core Architecture

The system operates as a synchronized pipeline:

1. **Static PE Analysis:** Extracts header features (entropy, sections, imports) before execution.
2. **Behavioral Engine:** Polls system events via Sysmon to monitor runtime activities.
3. **ML Inference:** Processes features through pre-trained models to generate a granular Risk Score.
4. **Action:** Triggers automated mitigation (e.g., process termination) if thresholds are exceeded.

---

## 📥 Getting Started

### Prerequisites
* Python 3.10+
* Sysmon (for behavioral data collection)

### Installation
```bash
# Clone the repository
git clone [https://github.com/SmartShield-AI/AI_Engine-Server.git](https://github.com/SmartShield-AI/AI_Engine-Server.git)
cd AI_Engine-Server

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
