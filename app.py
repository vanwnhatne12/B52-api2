from flask import Flask, request, jsonify, Response
import requests
import os

app = Flask(__name__)

# Khóa bí mật để truy cập API
SECRET_KEY = "ditmemaythichbucukhong"

# Route mặc định để kiểm tra hoạt động
@app.route("/")
def home():
    return "✅ B52 API của @VanwNhat đã chạy thành công trên Render!"

# API chính
@app.route("/api/lc79@VanwNhat", methods=["GET"])
def hidden_api():
    key = request.args.get("key")

    if key != SECRET_KEY:
        return Response(
            "Địt Con Mẹ Mày Api Của Văn Nhật Bú Cu Đi Rồi Admin Share Free @VanwNhat_Real",
            status=403,
            content_type="text/plain; charset=utf-8"
        )

    try:
        # Gọi API gốc
        response = requests.get("https://toolhth.site/b52th.php", headers={
            "X-Requested-With": "XMLHttpRequest"
        })
        data = response.json()

        # Trả kết quả định dạng JSON
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

# Chạy app với PORT do Render cấp
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))  # Render sẽ gán PORT tự động
    app.run(host="0.0.0.0", port=port)
