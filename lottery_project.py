import os
import random
from flask import Flask, render_template, jsonify, url_for

# 強制抓取檔案所在絕對路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_dir, "templates")
static_folder = os.path.join(current_dir, "static")

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

@app.route('/')
def index():
    try:
        # 這裡會強制找 templates/index.html
        return render_template('index.html')
    except Exception as e:
        return f"讀取網頁失敗，請檢查 templates 資料夾。錯誤訊息: {str(e)}"

@app.route('/draw')
def draw():
    try:
        # 圖片路徑：static/images/
        img_path = os.path.join(static_folder, "images")
        if not os.path.exists(img_path):
            return jsonify({"error": "找不到 static/images 資料夾"}), 404
            
        images = [f for f in os.listdir(img_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if not images:
            return jsonify({"error": "images 資料夾內沒有圖片"}), 404
            
        selected_image = random.choice(images)
        image_url = url_for('static', filename='images/' + selected_image)
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
