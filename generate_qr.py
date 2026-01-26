import os
import uuid
import qrcode

# 配置
GITHUB_PAGES_BASE = "https://sheep8787.github.io/Simple-QR-code-generator"
UPLOAD_DIR = "uploads"
QR_DIR = "qrcodes"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(QR_DIR, exist_ok=True)

def save_image(file_bytes, filename=None):
    """保存上传图片到 uploads/"""
    suffix = "png" if not filename else filename.split(".")[-1]
    image_name = f"{uuid.uuid4()}.{suffix}" if not filename else filename
    path = os.path.join(UPLOAD_DIR, image_name)
    with open(path, "wb") as f:
        f.write(file_bytes)
    return image_name, path

def generate_qr(image_name):
    """生成二维码，指向 GitHub Pages 上的图片"""
    image_url = f"{GITHUB_PAGES_BASE}/uploads/{image_name}"
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(image_url)
    qr.make(fit=True)

    qr_name = f"{uuid.uuid4()}.png"
    qr_path = os.path.join(QR_DIR, qr_name)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(qr_path)

    return image_url, f"{GITHUB_PAGES_BASE}/qrcodes/{qr_name}"

# 示例：上传一张本地图片
if __name__ == "__main__":
    # 读取本地测试图片
    with open("image_recognition.jpg", "rb") as f:
        file_bytes = f.read()

    image_name, _ = save_image(file_bytes, "image_recognition.jpg")
    image_url, qr_url = generate_qr(image_name)

    print("GitHub Pages Image URL:", image_url)
    print("QR Code URL:", qr_url)
