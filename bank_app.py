program_user = {
    'name': 'admin',
    'email': 'admin@vgg.com',
    'password': 'admin123',
    'balance': 0.0
}

new_program_user = {
    'name': '',
    'email': '',
    'password': '',
    'balance': 0.0
}

beneficiary = {
    'email': '',
    'balance': 0.0
}


# Create Account
def create_account():
    email_request = input('Please enter your email: ')
    if email_request == program_user['email']:
        return print('Already an existing user, log in')
    else:
        new_program_user['email'] = email_request

    password_request1 = input('Please enter your password: ')
    password_request2 = input('Please enter your password again: ')

    if password_request1 != password_request2:
        return print("Password Mismatch!. Try again!")
    else:
        new_program_user['password'] = password_request2

    print('Account Created Successfuly!')


# Transaction
def transaction():
    program_user
    password = input("Please key in your password: ")

    if password == program_user['password']:
        print('Access Granted')
        transaction_request = input("""
            Press 1 to check balance
            Press 2 for deposit
            Press 3 to withdraw
            Press 4 for transfer: """)

        # Check Balance
        if int(transaction_request) == 1:
            balance()

        # Deposit
        if int(transaction_request) == 2:
            deposit()

        # Withdraw
        if int(transaction_request) == 3:
            withdrawal()

        # Transfer
        if int(transaction_request) == 4:
            transfer()

    if password != str(program_user['password']):
        print("Authorized Personnel Only, please create account!")
        create_account()


# Check Balance
def balance():
    print("Your balance is: ₦ " + str(new_program_user['balance']))


# Deposit
def deposit():
    deposit_request = input('Please enter an amount deposit: ')
    new_program_user['balance'] += int(deposit_request)
    print("Your New Balance: ₦ " + str(new_program_user['balance']))


# Withdraw
def withdrawal():
    withdrawal_request = int(input('State here your withdrawal amount: '))

    if new_program_user['balance'] < withdrawal_request:
        print("Insufficient funds")
        deposit()
    if new_program_user['balance'] > withdrawal_request:
        print(
            f"Amount Withdrawn: ₦ {withdrawal_request}, Available Bal: ₦ {new_program_user['balance'] - withdrawal_request}")


# Transfer
def transfer():
    beneficiary_email = input('Email to Transfer to: ')
    beneficiary['email'] = beneficiary_email
    transfer_amount = int(input('Key in amount to transfer'))

    if program_user['balance'] < 0:
        deposit()

    beneficiary['balance'] = transfer_amount
    new_program_user['balance'] - transfer_amount
    print(f"Beneficiary A/c Bal: {beneficiary['balance']}")


print('\nWelcome to the VGG Banking Application Program!\n')
name = input('Please key in your name: ')
new_program_user['name'] = name
account_request = int(input(
    '\nGood Day ' + name + '.' + '\nPress 1 to create account or \nPress 2 to perform transaction: '))

if account_request == 1:
    create_account()


if account_request == 2:
    transaction()
