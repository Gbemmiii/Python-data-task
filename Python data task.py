import string
import random

print("Employee Database")
# initialize an empty list to store user data
data = []
# dictionary to store user data
user = {}

letters = string.ascii_lowercase #collected the ascii letters

while True:
    First_name = input("Input first name: ")  # prompt first name input 
    Last_name = input("Input last name: ")  # prompt second name
    break
# function to check email address
def checkEmail():
    email_address = input("Input your email address: ") 
    characters = "@."
    minlength = 6
    for i in characters: # check that '@' and '.' exist in the characters
        if i not in email_address: # loop through the email address to see if each character exist else prompt user to input again 
            email_address = input("Invalid email address \n Your email address  must have '{}' \n Please try again: ".format(i))     
    if len(email_address) <= minlength:
        email_address = input("Your email address is too short please try again: ")
    return email_address
Email = checkEmail()  # prompt user email address


# function to generate password collects the user first name and last name as an argument to work
def generatePassword(fname, sname):
    getfirstnameletters = fname[:2] #get the first two letter of first name
    getsecondnameletters = sname[:2]  # get the first two letter of last name
    password = getfirstnameletters + getsecondnameletters  # variable to store the password adds the first two letters of first and last name
    i = 0 # counter for the loop to randomly generate the 5 letters
    while i < 5:
        password += random.choice(letters) # randomly picks a letter from ascii letters called earlier and then adds it to the password variable
        i += 1 # increments the counter
    return password
password = generatePassword(First_name, Last_name)
print("Here is your password: ", password)

msg = input("Are you satisfied with the above password, enter yes or no: ")
if msg == "no":
	password = input("Please enter your preferred password: ")
if len(password) < 7:
    password = input("Password must have at least 7 characters, try again: ")
if len(password) >= 7:

    user['First_name'] = First_name
    user['Last_name'] = Last_name
    user['Email'] = Email
    user['password'] = password
    data.append(user)
    print(data) 

elif msg == "yes":
    
    user['First_name'] = First_name
    user['Last_name'] = Last_name
    user['Email'] = Email
    user['password'] = password
    data.append(user)
    print(data) 
