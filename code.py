from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uuid
import os
import qrcode

app = FastAPI()

# ========= 配置 =========
UPLOAD_DIR = "uploads"
QR_DIR = "qrcodes"

# ⚠️ 改成你的 cloudflared 公网地址（必须是 https）
PUBLIC_BASE = "https://induced-mud-identifies-castle.trycloudflare.com"
# ========================

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(QR_DIR, exist_ok=True)

# 静态文件访问
app.mount("/images", StaticFiles(directory=UPLOAD_DIR), name="images")
app.mount("/qr", StaticFiles(directory=QR_DIR), name="qr")


@app.get("/")
def root():
    return {"status": "ok", "msg": "service running"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # 生成唯一文件名
    suffix = file.filename.split(".")[-1]
    image_name = f"{uuid.uuid4()}.{suffix}"
    image_path = os.path.join(UPLOAD_DIR, image_name)

    # 保存图片
    with open(image_path, "wb") as f:
        f.write(await file.read())

    # 公网图片 URL（⚠️ 不能是 127.0.0.1）
    image_url = f"{PUBLIC_BASE}/images/{image_name}"

    # 生成二维码
    qr = qrcode.make(image_url)
    qr_name = f"{uuid.uuid4()}.png"
    qr_path = os.path.join(QR_DIR, qr_name)
    qr.save(qr_path)

    qr_url = f"{PUBLIC_BASE}/qr/{qr_name}"

    return JSONResponse({
        "image_url": image_url,
        "qr_url": qr_url
    })
