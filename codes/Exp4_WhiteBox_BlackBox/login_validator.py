# login_validator.py - Exp 4 worked "similar question" (Login form), V(G) = 6
USERS = {'johan23': 'Secure@123'}          # stand-in for the database

def user_exists(u):
    return u in USERS

def validate_login(username, password):
    if username == '':                      # D1
        return 'Username required'
    elif password == '':                    # D2
        return 'Password required'
    elif len(password) < 8:                 # D3
        return 'Password too short'
    elif not user_exists(username):         # D4
        return 'User not found'
    elif password != USERS[username]:       # D5
        return 'Invalid credentials'
    else:
        return 'Login successful'
