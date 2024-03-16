from flask import Flask
import random
import hashlib

app = Flask(__name__)


@app.get("/")
def hewoo():
    bytes = random.randbytes(100)
    return hashlib.sha256(bytes).hexdigest()
