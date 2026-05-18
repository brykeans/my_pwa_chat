# PWA Chat App (Python Flask + Firebase)

這是一個簡單的 PWA 聊天應用專案結構範例。

## 技術棧
- **Backend**: Python Flask
- **Frontend**: HTML, Bootstrap 5
- **PWA**: Service Worker, Web Manifest
- **Database**: Firebase Realtime Database

## 安裝步驟
1. 安裝套件: `pip install flask requests`
2. 執行應用: `python app.py`
3. 存取位址: `http://127.0.0.1:5000`

## Firebase 設定
目前使用 URL: `https://chat-app-136b8-default-rtdb.firebaseio.com/`
請確保 Firebase 規則已開啟為公讀/公寫 (僅限測試環境)。

## PWA 功能
- 可安裝至手機桌面 (需使用 HTTPS 或 localhost)。
- 支援離線快取基本頁面。