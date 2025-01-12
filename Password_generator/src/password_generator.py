import random
import string

# USER GREETINGS AND PARAMETERS #
print("----------------Welcome to Password Generator----------------")
length = int(input("Please enter the length desired for your password: ") or 10)
special_car = str(input('Would you like to use special characters in your password? ("yes" or "no"): ')or "yes")
special_sentence = str(input('Would you like to use a special sentence or word in your password? ("yes" or "no"): ')or "yes" )

# PASSWORD CREATION FUNCTIONS #
def password_C(length: int) -> str:  # Password generator with special characters
    password = ""
    all_characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password += random.choice(all_characters)
    return password

def password_no_S_C(length: int) -> str:  # Password generator with only regular letters from ASCII
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters)  
    return password

def password_S(length: int, sentence: str) -> str:  # Password generator with special sentence included
    password = sentence
    while len(password) < length:  
        password += random.choice(string.ascii_letters + string.digits) 
    return password[:length] 

def password_S_C(length: int, sentence: str) -> str:  # Password generator with special sentence and special characters included
    password = sentence
    all_characters = string.ascii_letters + string.digits + string.punctuation
    while len(password) < length: 
        password += random.choice(all_characters)  
    return password[:length] 



# Main loop for password creation
if special_car.lower() in ["no", "n"]:
    if special_sentence.lower() in ["yes", "y"]:
        special_word = str(input("Please enter the special sentence or word you want in your password: "))
        password = password_S(length, special_word)
        print(f'Your password with special sentence is: {password}')
    else:
        password = password_no_S_C(length)
        print(f'Your password is: {password}')
elif special_car.lower() in ["yes", "ye", "y"]:
    if special_sentence.lower() in ["yes", "y"]:
        special_word = str(input("Please enter the special sentence or word you want in your password: "))
        password = password_S_C(length, special_word)
        print(f"Your password with special characters and sentence is: {password}")
    else:
        password = password_C(length)
        print(f"Your password with special characters is: {password}")





