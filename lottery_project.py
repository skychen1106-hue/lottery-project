import os
import random
from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

# --- 自動路徑設定 ---
# 取得目前程式檔案 (lottery_project.py) 所在的目錄路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 預期圖片路徑應為：根目錄/static/images
IMAGE_FOLDER = os.path.join(BASE_DIR, 'static', 'images')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():
    try:
        # 檢查 static/images 資料夾是否存在
        if not os.path.exists(IMAGE_FOLDER):
            return jsonify({"error": f"找不到資料夾: {IMAGE_FOLDER}"}), 404
        
        # 取得所有圖檔 (忽略隱藏檔)
        images = [f for f in os.listdir(IMAGE_FOLDER) 
                 if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        if not images:
            return jsonify({"error": "images 資料夾內沒有圖片檔案"}), 404
        
        # 隨機抽取
        selected_image = random.choice(images)
        
        # 生成網址：對應到 static/images/檔名
        image_url = url_for('static', filename='images/' + selected_image)
        
        return jsonify({"image_url": image_url})
        
    except Exception as e:
        # 如果出錯，回傳具體的錯誤訊息幫助除錯
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # 本地端測試用
    app.run(host='0.0.0.0', port=8000)
