import re

def validasi_password(password):
    return (len(password) >= 8 and
            ' ' not in password and
            bool(re.search(r'[A-Z]', password)) and
            bool(re.search(r'\d', password)) and
            bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password)))
