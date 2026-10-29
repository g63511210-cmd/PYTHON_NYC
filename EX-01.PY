# Password Check: Write a program which ask user to give a password and check if the password is strong. A strong password will have at least 8 characters, upper and lower case characters, digits, and special characters (!@#$%^&), at least one of each category. 

password=input('give me a password')
## check whetehr its strong with the requirements 
 
characters=False
upper_case=False
lower_case=False
digits=False
special_characters=False
for charac in password:
    if charac >='A' and charac <='Z':
        upper_case= True
    elif charac >= 'a' and charac<='z':
        lower_case=True
    elif charac >='0' and charac <= '9':
        digits=True
    elif charac == "!@#$%^&":
        speacial_characters=True

        if len(password) >=8:
            characters = True

            if characters == upper_case and lower_case and digits and special_characters:
             print ('strong password')
            else:
                print ('not strong password')

