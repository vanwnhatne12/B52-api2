from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

# 🔐 Key bí mật
SECRET_KEY = "bucacditme"

# ✅ Route test root
@app.route("/")
def home():
    return "✅ B52 API của @VanwNhat đã chạy thành công trên Render!"

# ✅ Route chính
@app.route("/api/b52th@VanwNhat", methods=["GET"])
def hidden_api():
    key = request.args.get("key")

    if key != SECRET_KEY:
        return Response(
            "Địt Con Mẹ Mày Api Của Văn Nhật Bú Cu Đi Rồi Admin Share Free @VanwNhat_Real",
            status=403,
            content_type="text/plain; charset=utf-8"
        )

    try:
        # ⚠️ Thêm User-Agent để tránh bị chặn
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36"
        }

        response = requests.get(
            "https://toolhth.site/b52th.php",
            headers=headers,
            timeout=5  # Giới hạn thời gian kết nối
        )

        data = response.json()

        result = {
            "phien": data.get("current_session"),
            "ket_qua": data.get("current_result"),
            "phien_sau": data.get("next_session"),
            "du_doan": data.get("prediction"),
            "id": "Tele_VanwNhatReal"
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": "Không thể truy cập API gốc.",
            "chi_tiet": str(e)
        }), 500

# ✅ Khởi chạy app Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
