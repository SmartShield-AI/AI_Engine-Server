from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

# 🔹 Your existing modules (flat structure)
from hash_file import hash_file
from cloud_based import vt_check_hash, check_hash_malwarebazaar
from ember_file_analyze import ember_analyze_file
from custom_file_analyze import custom_analyze_file

app = FastAPI(title="SmartShield AI Server 🚀")

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================
# 🔹 1. HASH-ONLY API
# =========================
class HashRequest(BaseModel):
    hash: str
    use_vt: bool = True
    use_mb: bool = True


@app.post("/analyze/hash")
def analyze_hash(data: HashRequest):
    result = {}

    if data.use_vt:
        result["vt"] = vt_check_hash(data.hash)

    if data.use_mb:
        result["mb"] = check_hash_malwarebazaar(data.hash)

    return result


# =========================
# 🔹 2. FILE UPLOAD API (FULL ANALYSIS)
# =========================
@app.post("/analyze/file")
def analyze_file(
    file: UploadFile = File(...),
    use_vt: bool = True,
    use_mb: bool = True,
    use_cust: bool = False,
    use_ember: bool = True,
):
    result = {}

    # 🔹 Save uploaded file temporarily
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # 🔹 Generate hash
        file_hash = hash_file(file_path)
        result["hash"] = file_hash

        # 🔹 VirusTotal
        if use_vt:
            result["vt"] = vt_check_hash(file_hash)

        # 🔹 MalwareBazaar
        if use_mb:
            result["mb"] = check_hash_malwarebazaar(file_hash)

        # 🔹 Custom ML Model
        if use_cust:
            result["custom"] = custom_analyze_file(file_path)

        # 🔹 EMBER Model
        if use_ember:
            result["ember"] = ember_analyze_file(file_path)

    except Exception as e:
        result["error"] = str(e)

    finally:
        # 🔹 Clean up file after processing
        if os.path.exists(file_path):
            os.remove(file_path)

    return result


# =========================
# 🔹 HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {"message": "SmartShield AI Server Running 🚀"}
