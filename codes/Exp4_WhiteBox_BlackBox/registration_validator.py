# registration_validator.py  - Exp 4 (manual's form, pseudocode turned into Python)
import re

def validate_form(username, password, email, phone=None):
    errors = []
    # D1 - username length 3-20
    if len(username) < 3 or len(username) > 20:
        errors.append('Invalid username length')
    # D2 - username alphanumeric
    elif not username.isalnum():
        errors.append('Username must be alphanumeric')
    # D3 - password length 8-16
    if len(password) < 8 or len(password) > 16:
        errors.append('Password: invalid length')
    # D4 - uppercase
    elif not any(c.isupper() for c in password):
        errors.append('Password: needs uppercase')
    # D5 - digit
    elif not any(c.isdigit() for c in password):
        errors.append('Password: needs digit')
    # D6 - special char
    elif not any(not c.isalnum() for c in password):
        errors.append('Password: needs special character')
    # D7 - email format
    if not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', email):
        errors.append('Invalid email format')
    # phone: exactly 10 digits starting 6-9 (optional field in this function)
    if phone is not None and not re.fullmatch(r'[6-9]\d{9}', phone):
        errors.append('Invalid phone number')
    return 'Registration Successful' if not errors else errors
# V(G) = 7 decisions + 1 = 8 (manual count)

if __name__ == '__main__':
    print(validate_form('john1', 'Abcd1@ef', 'a@b.c', '9876543210'))
    print(validate_form('jo', 'abc', 'bad-email'))
