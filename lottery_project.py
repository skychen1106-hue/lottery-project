import os
import random
from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # 檢查路徑的偵錯工具
    base_path = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_path, 'templates', 'index.html')
    
    if not os.path.exists(template_path):
        # 如果找不到網頁，直接在螢幕印出目前的目錄結構
        files_in_root = os.listdir(base_path)
        return f"ERROR: 找不到 index.html。<br>目前目錄位置: {base_path}<br>目錄下的檔案有: {files_in_root}"
    
    return render_template('index.html')

@app.route('/draw')
def draw():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_folder = os.path.join(base_path, 'static', 'images')
        
        if not os.path.exists(image_folder):
            return jsonify({"error": f"找不到圖片資料夾: {image_folder}"}), 404
            
        images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if not images:
            return jsonify({"error": "images 內沒圖片"}), 404
            
        selected_image = random.choice(images)
        image_url = url_for('static', filename='images/' + selected_image)
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
