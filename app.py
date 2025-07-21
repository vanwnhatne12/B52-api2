from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

SECRET_KEY = "ditmemaythichbucukhong"  # Key bí mật bạn đặt

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
        response = requests.get("https://toolhth.site/b52th.php", headers={"X-Requested-With": "XMLHttpRequest"})
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

# Render sẽ dùng PORT từ biến môi trường
import os
if name == "main":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
