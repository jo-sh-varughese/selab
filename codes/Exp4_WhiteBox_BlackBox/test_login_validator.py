# test_login_validator.py - basis-path tests, one per independent path (V(G)=6)
import pytest
from login_validator import validate_login

@pytest.mark.parametrize('tc,u,p,expected', [
    ('TC-WB-01', '', 'Secure@123', 'Username required'),
    ('TC-WB-02', 'johan23', '', 'Password required'),
    ('TC-WB-03', 'johan23', 'abc12', 'Password too short'),
    ('TC-WB-04', 'ghost99', 'Secure@123', 'User not found'),
    ('TC-WB-05', 'johan23', 'Wrong@123', 'Invalid credentials'),
    ('TC-WB-06', 'johan23', 'Secure@123', 'Login successful'),
])
def test_paths(tc, u, p, expected):
    assert validate_login(u, p) == expected
