# 1A. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def program():
    sample_string = 'The quick Brown Fox'
    upper_str_receiver = ''
    lower_str_receiver = ''
    
    for letter in sample_string:
        if letter.isupper() == True:
            upper_str_receiver += letter
        elif letter.islower() == True:
            lower_str_receiver += letter

    print(f"No. of Upper case Characters: {len(upper_str_receiver)}")
    print(f"No. of Lower case Characters: {len(lower_str_receiver)}")

program()


# 1B. Write a Python function to find the Max of three numbers ------------------------------------------------

def program(*args):
    return max(args)

program(1000, 2000, 3000)

# Result --> 3000


# 2. Write a Python function that takes a number as a parameter and check the number is prime or not.

def program():
    num = int(input('Key in a number: '))
    num_len_list = list(range(1, num + 1))
    num_len = len(list(range(1, num + 1)))
    empty_list = []

    for i in num_len_list:
        if len(num_len_list) % i == 0:
            empty_list.append(i)

    if empty_list == [empty_list[0], empty_list[-1]]:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

program()
