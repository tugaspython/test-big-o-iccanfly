 def validasi_password(password: str) -> bool:
     """True jika password >=8, ada huruf besar, angka, simbol, dan tidak mengandung spasi."""
     if len(password) < 8:
         return False
     has_upper = has_digit = has_symbol = False
     for c in password:
         if c.isspace():
             return False
         if c.isupper():
             has_upper = True
         if c.isdigit():
             has_digit = True
         if not c.isalnum():
             has_symbol = True
         if has_upper and has_digit and has_symbol:
             return True
     return False
