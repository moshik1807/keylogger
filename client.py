from encryptor import Encryptor
import requests

# יצירת אובייקט Encryptor עם המפתח המתאים (כמו שכתבת קודם)
encryptor = Encryptor(42)

# המידע שברצונך לשלוח (למשל, לחץ מקש)
data = "Some sensitive information"
# הצפנה של המידע
encrypted_data = encryptor.encrypt(data)
print("Encrypted Data:", encrypted_data)

# שליחת המידע לשרת
response = requests.post("http://127.0.0.1:8080/receive_data", json={
    "data": encrypted_data,
    "machine_name": "Machine1"
})

# תצוגת תגובת השרת
print(response.json())

