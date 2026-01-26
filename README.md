
# Simple QR Code Generator

## 项目简介
这是一个基于 FastAPI 的简单网页服务，用户可以上传图片，自动生成二维码，扫码即可访问图片。二维码已在微信和 QQ 上测试，均可正常访问。

## 功能特点
- 上传图片自动生成二维码
- 生成的二维码可在微信和 QQ 扫码访问
- 图片和二维码都托管在 GitHub Pages 上，稳定可访问
- 支持 PNG、JPG、JPEG、GIF 格式

## 文件结构

.
├── uploads/ # 上传的图片
├── qrcodes/ # 生成的二维码
├── code.py # FastAPI 主程序
├── generate_qr.py # 批量生成二维码脚本
└── README.md

## 使用说明
1. 克隆仓库到本地：
```bash
git clone https://github.com/sheepO2/Simple-QR-code-generator.git

2. 安装依赖：
pip install fastapi uvicorn qrcode pillow

3. 运行服务：
python code.py

4. 上传图片生成二维码：
·访问本地接口 http://127.0.0.1:8000/upload 上传图片
·或者直接运行 generate_qr.py 生成最新上传图片的二维码

5. GitHub Pages 访问：
·图片 URL 示例：https://your_username.github.io/Simple-QR-code-generator/uploads/your_image.jpg
·二维码 URL 示例：https://your_username.github.io/Simple-QR-code-generator/qrcodes/your_qr.png

注意事项：
·请确保二维码内容指向 GitHub Pages 的公网 URL，而非本地 IP
·微信和 QQ 均可扫码访问，但部分版本 QQ 扫码直接访问图片可能不稳定，推荐用 HTML 页面包裹图片
