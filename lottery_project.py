import os
import random
from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

# 自動定位：確保在雲端環境也能找到正確的 static 資料夾
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 修正路徑拼接，確保與 GitHub 結構一致
IMAGE_FOLDER = os.path.join(BASE_DIR, 'static', 'images')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():
    try:
        # 如果資料夾不存在，回傳詳細路徑以便除錯
        if not os.path.exists(IMAGE_FOLDER):
            return jsonify({"error": f"找不到路徑: {IMAGE_FOLDER}"}), 404
        
        # 讀取圖片清單
        images = [f for f in os.listdir(IMAGE_FOLDER) 
                 if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        if not images:
            return jsonify({"error": "images 資料夾內是空的"}), 404
        
        selected_image = random.choice(images)
        # 使用 url_for 確保產生的網址符合雲端規範
        image_url = url_for('static', filename='images/' + selected_image)
        
        return jsonify({"image_url": image_url})
    except Exception as e:
        # 將具體報錯傳回前端，避免只有冷冰冰的 500 錯誤
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
