# Question 18
# Level 3
# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345,Manzoor#1
# Then, the output of the program should be:
# ABd1234@1
# password = (input("Enter identity number: "))
names = input("Enter passwords: ").split(',')
# print(names)
# name = "Manzoor#1"
# if 
for name in names:
    # print(name)
    lower = ''
    upper = ''
    special = ''
    digit = ''
    for char in name:
        if char.isupper() :
            upper += "U"
        if char.islower():
            lower += 'L'
        if char in "#$@":
            special += 'S'
        if char.isdigit():
            digit += 'D'

    result = lower + upper + special + digit
    # print(result)
    # print(result)
    if "L" in result and  "U" in result and  "S" in result and "D" in result and len(result) >= 6 and len(result) <=12:
    # if set("LUSD") in result and len(result) >= 6 and len(result) <=12:
        print("yes")
    else:
        print("no")
    result = ''
    lower = ''
    upper = ''
    special = ''
    digit = ''
# print("m" in name)