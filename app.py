from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Update these with your email settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'kefidee@gmail.com'
EMAIL_PASSWORD = 'KefasiChijaka2nd'  # Use an app password if using Gmail

@app.route('/')
def index():
    return 'MoveInn Flask backend running!'

@app.route('/submit-onboarding', methods=['POST'])
def submit_form():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    role = data.get('role')  # 'Buyer' or 'Seller'
    message = data.get('message')

    content = f"""New Onboarding Submission:
    Name: {name}
    Email: {email}
    Role: {role}
    Message: {message}
    """

    # Send email
    try:
        msg = MIMEText(content)
        msg['Subject'] = f'New {role} Onboarding - {name}'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify ({"message": "Form submitted and emailed successfully."}), 200

    except Exception as e:
        print("Error sending email:", e)
        return jsonify({"error": "Email failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
