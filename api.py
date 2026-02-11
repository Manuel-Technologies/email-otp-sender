from flask import Flask, request, jsonify
from main import send_otp_email

app = Flask(__name__)

@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json()
    if not data or "recipient_email" not in data or "subject" not in data or "otp" not in data:
        return jsonify({"error": "Invalid request"}), 400

    recipient_email = data["recipient_email"]
    subject = data["subject"]
    otp = data["otp"]

    try:
        send_otp_email(recipient_email, subject, otp)
        return jsonify({"message": "OTP sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
