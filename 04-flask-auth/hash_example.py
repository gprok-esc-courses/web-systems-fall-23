from flask_bcrypt import Bcrypt
from flask import Flask


app = Flask(__name__)
bcrypt = Bcrypt(app)

password = "1234"
hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

print(hash_password)

is_ok = bcrypt.check_password_hash(hash_password, '12345')
print(is_ok)

