from abc import ABC, abstractmethod

class IWriter(ABC):
    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        pass

class FileWriter(IWriter):
    def __init__(self, file_path: str):
        self.file_path = file_path