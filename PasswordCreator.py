import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = input("Master Password: ").encode()

# Get path to script file
path = os.path.abspath(os.path.dirname(__file__))

salt = os.urandom(16)
with open(path + "/salt", "wb") as file:
    file.write(salt)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

def encrypt(prompt: str) -> bytes:
    return f.encrypt(input(prompt).encode())

slatePass = encrypt("\nSlate Password: ")
githubPass = encrypt("Github Password: ")
visualStudioPass = encrypt("Visual Studio Password: ")
unityPass = encrypt("Unity Password: ")
miroPass = encrypt("Miro Password: ")

def writePass(pw: bytes, dbFile):
    dbFile.write(len(pw).to_bytes()) # Only 1 byte
    dbFile.write(pw)

with open(path + "/db", "wb") as db:
    writePass(slatePass, db)
    writePass(githubPass, db)
    writePass(visualStudioPass, db)
    writePass(unityPass, db)
    writePass(miroPass, db)

print("\nPasswords saved. Upload this entire folder as a zip.")

with open(path + "/db", "rb") as readDB:
    for i in range(5):
        print(f.decrypt(readDB.read(int.from_bytes(readDB.read(1)))).decode())

#msg = f.decrypt(token).decode()
#print(msg)