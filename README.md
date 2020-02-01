# vgg_assignment

Assignment 1: Banking App CLI

Build a command-line Banking Application with the following functionalities:

Application starts with a prompt to the user with the following options:

Press 1: create account
    Create account: This should prompt you to enter an email/or unique identity, and then a password. You must check your data structure to make sure the account is unique before creating the new account

Press 2: transaction
    Transaction: Authenticate the user by prompting for a password. 
    
    if the password is correct, user is authenticated and show the following options:
        Press 1: check balance
        Press 2: deposit
        Press 3: withdraw
        Press 4: transfer

        check balance: query your data structure to check the balance of the authenticated user

        deposit: prompt the user to enter an amount, then add the amount to the users balance

        withdraw: prompt the user to enter an amount, if the user does not have money in their account, tell them to deposit and move to the deposit prompt. If they user has money, print out the amount withdrawn and the available balance.

        transfer: prompt the user to enter an email of the person they want to transfer to, prompt for the amount, deduct the amount from the authenticated users balance, add the amount to the beneficiaries account,

        Ensure that you clog all the gaps for those process flows that i have not explicitly defined

    if the password is incorrect, tell the user that they are not authorized and go back to the create account option
