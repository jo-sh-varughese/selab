# test_registration_validator.py - EP, BVA and White-box path tests (Exp 4)
import pytest
from registration_validator import validate_form

OK = 'Registration Successful'
GOOD_PWD, GOOD_MAIL = 'Abcd1@ef', 'a@b.c'

# ---------- White-box: one test per independent path (V(G)=8) ----------
@pytest.mark.parametrize('u,p,e,expected', [
    ('john1', GOOD_PWD, GOOD_MAIL, OK),                                   # WB-01 all valid
    ('jo',    GOOD_PWD, GOOD_MAIL, ['Invalid username length']),          # WB-02 D1 true
    ('john@1', GOOD_PWD, GOOD_MAIL, ['Username must be alphanumeric']),   # WB-03 D2 true
    ('john1', 'Ab1@', GOOD_MAIL, ['Password: invalid length']),           # WB-04 D3 true
    ('john1', 'abcd1@ef', GOOD_MAIL, ['Password: needs uppercase']),      # WB-05 D4 true
    ('john1', 'Abcde@fg', GOOD_MAIL, ['Password: needs digit']),          # WB-06 D5 true
    ('john1', 'Abcde1fg', GOOD_MAIL, ['Password: needs special character']), # WB-07 D6
    ('john1', GOOD_PWD, 'abc.com', ['Invalid email format']),             # WB-08 D7 true
])
def test_paths(u, p, e, expected):
    assert validate_form(u, p, e) == expected

# ---------- BVA: password length 8-16 ----------
@pytest.mark.parametrize('pwd,valid', [
    ('Abcde1@', False), ('Abcde1@f', True), ('Abcde1@fg', True),
    ('Abcde1@fghijklm', True), ('Abcde1@fghijklmn', True), ('Abcde1@fghijklmno', False),
])
def test_password_bva(pwd, valid):
    assert (validate_form('john1', pwd, GOOD_MAIL) == OK) == valid

# ---------- BVA: username length 3-20 ----------
@pytest.mark.parametrize('n,valid', [(2, False), (3, True), (4, True), (19, True), (20, True), (21, False)])
def test_username_bva(n, valid):
    assert (validate_form('a' * n, GOOD_PWD, GOOD_MAIL) == OK) == valid

# ---------- EP: phone ----------
@pytest.mark.parametrize('ph,valid', [
    ('9876543210', True), ('987654321', False), ('98765432101', False),
    ('5876543210', False), ('98765abcde', False),
])
def test_phone_ep(ph, valid):
    assert (validate_form('john1', GOOD_PWD, GOOD_MAIL, ph) == OK) == valid

def test_multiple_errors_collected():
    r = validate_form('jo', 'abc', 'bad')
    assert len(r) == 3
