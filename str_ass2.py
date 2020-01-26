# 1A. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

sample_string = 'The quick Brown Fox'
upper_str_receiver = ''
lower_str_receiver = ''

def program():
    global upper_str_receiver
    global lower_str_receiver

    for letter in sample_string:
        if letter.isupper() == True:
            upper_str_receiver += letter
        elif letter.islower() == True:
            lower_str_receiver += letter

            
program()

print(f"No. of Upper case Characters: {len(upper_str_receiver)}")
print(f"No. of Lower case Characters: {len(lower_str_receiver)}")



# 1B. Write a Python function to find the Max of three numbers ------------------------------------------------

def program(*args):
    return max(args)

program(1000, 2000, 3000)

# Result --> 3000


# 2. Write a Python function that takes a number as a parameter and check the number is prime or not.
