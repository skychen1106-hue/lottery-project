import os
import random
from flask import Flask, render_template, jsonify, url_for

# 這裡特別指定 template 和 static 的路徑
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    # 檢查 index.html 是否真的在那裡，如果不在就噴出錯誤訊息給你看
    html_path = os.path.join(template_dir, 'index.html')
    if not os.path.exists(html_path):
        return f"錯誤：找不到 index.html。預期路徑在: {html_path}"
    return render_template('index.html')

@app.route('/draw')
def draw():
    try:
        image_folder = os.path.join(static_dir, 'images')
        if not os.path.exists(image_folder):
            return jsonify({"error": "找不到圖片資料夾"}), 404
        
        images = [f for f in os.listdir(image_folder) 
                 if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        if not images:
            return jsonify({"error": "images 內沒有圖"}), 404
        
        selected_image = random.choice(images)
        image_url = url_for('static', filename='images/' + selected_image)
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
