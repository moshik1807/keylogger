class Encryptor:
    def __init__(self, key: int):
        self.key = key

    def encrypt(self, data: str) -> str:
        return "".join(chr(ord(char) ^ self.key) for char in data)