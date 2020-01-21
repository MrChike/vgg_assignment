program_user = {
    'name': 'chike',
    'email': 'chike.egonu@venturegardenng.com',
    'password': 'chike123',
    # Lol, Broke Ass Nigga
    'balance': 0.0
}

new_program_user = program_user

beneficiary = {
    'email': '',
    'balance': 0.0
}

welcome_message = 'Welcome to the VGG Banking Application Program!\n'
print(welcome_message)
name = input('Please key in your name: ')
program_user['name'] = name
account_request = int(input(
    'Good Day ' + name + '. Press 1 to create account or Press 2 to perform transaction: '))


# Create Account
def create_account():
    email_request = input('Please enter your email: ')
    password_request1 = input('Please enter your password: ')
    password_request2 = input('Please enter your password again: ')

    if password_request1 == password_request2:
        program_user['password'] = password_request2

    if email_request != program_user['email']:
        program_user['email'] = email_request
        print('Account Created Successfuly!')
    else:
        print('Already an existing user, log in')


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
        withdrawal()
    if new_program_user['balance'] > withdrawal_request:
        print(
            f"Amount Withdrawn: {withdrawal_request}, Available Bal: {new_program_user['balance'] - withdrawal_request}")


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


if account_request == 1:
    create_account()


if account_request == 2:
    password = input("Please key in your password: ")

    if password == new_program_user['password']:
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


print('Static Database: ', f'{str(program_user)}')
