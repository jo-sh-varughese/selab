# test_bank_account.py
import pytest
from bank_account import BankAccount, InsufficientFundsError

@pytest.fixture
def account():
    """Fresh account with Rs.1000 for every test."""
    return BankAccount("Johan", 1000)

class TestCreate:
    def test_initial_balance(self):
        acc = BankAccount("Asha", 500)          # Arrange + Act
        assert acc.balance == 500                # Assert

    def test_empty_owner_raises(self):
        with pytest.raises(ValueError, match="Owner name required"):
            BankAccount("", 100)

    def test_negative_opening_balance_raises(self):
        with pytest.raises(ValueError):
            BankAccount("Asha", -1)

class TestDeposit:
    def test_deposit_increases_balance(self, account):
        assert account.deposit(500) == 1500

    @pytest.mark.parametrize("bad", [0, -1, -100])
    def test_non_positive_deposit_raises(self, account, bad):
        with pytest.raises(ValueError):
            account.deposit(bad)

    def test_string_deposit_raises(self, account):
        with pytest.raises(TypeError):
            account.deposit("500")

class TestWithdraw:
    @pytest.mark.parametrize("amt,expected", [
        (1, 999), (999, 1), (1000, 0),          # boundary values
    ])
    def test_valid_withdraw(self, account, amt, expected):
        assert account.withdraw(amt) == expected

    def test_zero_withdraw_raises(self, account):
        with pytest.raises(ValueError, match="positive"):
            account.withdraw(0)

    def test_overdraw_raises(self, account):
        with pytest.raises(InsufficientFundsError):
            account.withdraw(1001)               # max + 1

class TestTransfer:
    def test_transfer_moves_money(self, account):
        other = BankAccount("Priya", 0)
        account.transfer(other, 300)
        assert account.balance == 700
        assert other.balance == 300

    def test_failed_transfer_changes_nothing(self, account):
        other = BankAccount("Priya", 0)
        with pytest.raises(InsufficientFundsError):
            account.transfer(other, 5000)
        assert account.balance == 1000 and other.balance == 0
