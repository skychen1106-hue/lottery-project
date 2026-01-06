from flask import Flask, render_template, jsonify
import os
import random

# 強制鎖定桌面路徑
base_dir = r"C:\Users\sky.chen\Desktop\lottety_ project"

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():
    img_dir = os.path.join(base_dir, 'static', 'images')
    if not os.path.exists(img_dir):
        return jsonify({"error": "找不到圖片資料夾"}), 404
    
    images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not images:
        return jsonify({"error": "裡面沒圖片"}), 404
        
    selected = random.choice(images)
    return jsonify({"image_url": f"/static/images/{selected}"})

if __name__ == '__main__':
    # 使用 8000 port 以防 5000 被系統佔用
    app.run(host='127.0.0.1', port=8000, debug=False)
