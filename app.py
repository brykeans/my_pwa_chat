from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests

app = Flask(__name__)
# 必須設定 secret_key 才能使用 session 功能，這會解決您登入狀態失效的問題
app.secret_key = "secret_key_054" 

# Firebase URL (請確保此網址與您的 Firebase 控制台一致)
FIREBASE_URL = "https://chat11314310042-default-rtdb.firebaseio.com/"

@app.route('/')
def index():
    # 如果已經登入，直接導向留言板，不顯示登入頁面
    if 'user' in session:
        return redirect(url_for('board'))
    return render_template('login.html')

# 處理登入動作的路由
@app.route('/login_action', methods=['POST'])
def login_action():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # 這裡實作簡單驗證
    if username and password:
        session['user'] = username  # 將帳號存入 session
        return redirect(url_for('board'))
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)  # 登出時移除 session 紀錄
    return redirect(url_for('index'))

@app.route('/board')
def board():
    # 安全檢查：沒登入就踢回首頁
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('board.html')

@app.route('/register')
def register():
    return render_template('register.html')

# --- 新增：處理 Screen4 修改密碼的路由 ---
@app.route('/settings')
def settings():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('settings.html')

@app.route('/update_password', methods=['POST'])
def update_password():
    if 'user' not in session:
        return redirect(url_for('index'))
    
    # 獲取表單傳來的資料
    old_pw = request.form.get('old_password')
    new_pw = request.form.get('new_password')
    confirm_pw = request.form.get('confirm_password')
    
    # 這裡可以加入檢查邏輯，例如：
    if new_pw != confirm_pw:
        # 如果兩次新密碼不一致，可以導回並提示（這裡簡單處理直接導回）
        return redirect(url_for('settings'))
    
    # 實作密碼更新至 Firebase 的邏輯可寫在這裡
    # ...
    
    return redirect(url_for('board')) # 更新完回到留言板

# API: 獲取留言
@app.route('/api/messages', methods=['GET'])
def get_messages():
    response = requests.get(f"{FIREBASE_URL}/messages.json")
    return jsonify(response.json())

# API: 發送留言
@app.route('/api/messages', methods=['POST'])
def send_message():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    data['user'] = session['user'] # 強制使用 session 裡的帳號發言
    response = requests.post(f"{FIREBASE_URL}/messages.json", json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5000)