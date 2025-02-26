from abc import ABC, abstractmethod

class IWriter(ABC):
    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        pass

class FileWriter(IWriter):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def send_data(self, data: str, machine_name: str) -> None:
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.write(f"{machine_name}: {data}\n")
        except Exception as e:
            print(f"שגיאה בכתיבה לקובץ: {e}")