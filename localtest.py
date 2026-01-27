from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uuid
import os
import qrcode

app = FastAPI()

UPLOAD_DIR = "uploads"
QR_DIR = "qrcodes"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(QR_DIR, exist_ok=True)

# 静态文件访问
app.mount("/images", StaticFiles(directory=UPLOAD_DIR), name="images")
app.mount("/qr", StaticFiles(directory=QR_DIR), name="qr")


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    suffix = file.filename.split(".")[-1]
    image_name = f"{uuid.uuid4()}.{suffix}"
    image_path = os.path.join(UPLOAD_DIR, image_name)

    with open(image_path, "wb") as f:
        f.write(await file.read())

    # ⚠️ 关键：这里必须是“公网可访问的地址”
    image_url = f"http://127.0.0.1:8000/images/{image_name}"

    qr = qrcode.make(image_url)
    qr_name = f"{uuid.uuid4()}.png"
    qr_path = os.path.join(QR_DIR, qr_name)
    qr.save(qr_path)

    return JSONResponse({
        "image_url": image_url,
        "qr_url": f"http://127.0.0.1:8000/qr/{qr_name}"
    })
