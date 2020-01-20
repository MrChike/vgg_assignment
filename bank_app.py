program_user = {
    'name': 'chike',
    'email': 'chikeegonu@gmail.com',
    'password': 'chike123',
    'balance': 0.0
}


def program():
    welcome_message = 'Welcome to the VGG Banking Application Program!\n'
    print(welcome_message)
    name = input('Please key in your name: ')
    program_user['name'] = name
    account_request = int(input(
        'Good Day ' + name + '. Press 1 to create account or Press 2 to perform transaction: '))

    def create_account():
        if account_request == 1:
            email_request = input('Please enter your email: ')
            password_request1 = input('Please enter your password: ')
            password_request2 = input('Please enter your password again: ')

            if password_request1 == password_request2:
                program_user['password'] = password_request2

            if email_request not in program_user:
                program_user['email'] = email_request
                print('Account Created Successfuly!')
            else:
                print('Already an existing user, log in')

    create_account()

    def transaction():
        if account_request == 2:
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
                    print("Your balance is: ₦ " + str(program_user['balance']))

                # Deposit
                if int(transaction_request) == 2:
                    def deposit():
                        deposit_request = input('Please enter an amount: ')
                        program_user['balance'] += int(deposit_request)
                        print("Your New Balance: ₦ " +
                              str(program_user['balance']))
                    return deposit()

                # Withdraw
                if int(transaction_request) == 3:
                    def withdrawal():
                        withdrawal_request = input(
                            'State here your withdrawal amount: ')
                        if program_user['balance'] <= 0:
                            return deposit()
                    return withdrawal()

                # Transfer
                if int(transaction_request) == 4:
                    print('Action: 1: Transfer')

            if password != program_user['password']:
                return create_account()

    transaction()
