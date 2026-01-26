import os
import uuid
import qrcode
from datetime import datetime

# ---------------------- 配置 ----------------------
# GitHub Pages 基础 URL
GITHUB_PAGES_BASE = "https://sheepO2.github.io/Simple-QR-code-generator"

# 本地目录
UPLOAD_DIR = "uploads"
QR_DIR = "qrcodes"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(QR_DIR, exist_ok=True)


# ---------------------- 找到最新上传的图片 ----------------------
def get_latest_image():
    files = [f for f in os.listdir(UPLOAD_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not files:
        return None
    # 根据修改时间排序
    files.sort(key=lambda f: os.path.getmtime(os.path.join(UPLOAD_DIR, f)), reverse=True)
    return files[0]


# ---------------------- 生成二维码 ----------------------
def generate_qr(image_filename):
    image_url = f"{GITHUB_PAGES_BASE}/uploads/{image_filename}"
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(image_url)
    qr.make(fit=True)

    qr_name = f"{uuid.uuid4()}.png"
    qr_path = os.path.join(QR_DIR, qr_name)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img.save(qr_path)

    print(f"Image URL: {image_url}")
    print(f"QR Code saved at: {qr_path}")


# ---------------------- 主程序 ----------------------
if __name__ == "__main__":
    latest_image = get_latest_image()
    if not latest_image:
        print("No images found in 'uploads/' folder.")
    else:
        print(f"Latest image found: {latest_image}")
        generate_qr(latest_image)
