# 1) Basic list operations

# ROUNDS = 5
# numbers = []
#
# for x in range(ROUNDS):
#     user_numbers = int(input("Number: "))
#     numbers.append(user_numbers)
#
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# print(f"The smallest number is {min(numbers)}")
# print(f"The largest number is {max(numbers)}")
#
# print(f"The average of the number is {sum(numbers) / len(numbers)}")


# 2) Woefully inadequate security checker

# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
#              'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
#
# authorise_user = input("Username: ")
# if authorise_user in usernames:
#     print("Access Granted")
# else:
#     print("Access Denied")