# 銀行システムにおけるカスタム例外処理: カスタム例外クラス `BankValidationError` を作成し、
# これを継承した `BankMoneyError` と `BankAccountError` を定義します。
# これらの例外は、アカウントの検証や残高不足の検証に使用され、例外が発生すると詳細なエラーメッセージが表示されます。
#
# Custom Exception Handling in Bank System: Create a custom exception class `BankValidationError`,
# and define `BankMoneyError` and `BankAccountError` inheriting from it.
# These exceptions are used for account validation and insufficient balance checks,
# providing detailed error messages when raised.

# Example: Bank System with Custom Exception Handling

account = [
    {
        "name": "taro",
        "cardNumber": "1111-1111-1111-1111",
    },
    {
        "name": "jiro",
        "cardNumber": "2222-2222-2222-2222",
    },
]

bank_money = 1000000


# Define custom exception classes
class BankValidationError(Exception):
    name = None
    detail = None

    def __str__(self):
        return f"{self.name}: {self.detail}"


class BankMoneyError(BankValidationError):
    name = "BankMoneyError"
    detail = "bank money is not enough"


class BankAccountError(BankValidationError):
    name = "BankAccountError"
    detail = "bank account is not found"


# Function to validate account
def validate_account(account_name, account):
    for a in account:
        if a["name"] == account_name:
            return a
    raise BankAccountError


# Function to validate money
def validate_money(money):
    if bank_money < money:
        print(f"{bank_money - money}円足りません")
        raise BankMoneyError


# Try to validate account and money
try:
    account_name = "taro"
    account = validate_account(account_name, account)
    validate_money(100000000)
    print("検証完了")
except BankValidationError as e:
    print(e)
