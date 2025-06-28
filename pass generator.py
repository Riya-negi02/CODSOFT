import random
import string
def generate_random_password(length):
    if length<0:
        raise ValueError("The number of digits should be positive")
    characters= string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choices(characters, k= length ))
    return password

    
try:   
    number= int(input("Enter no. of digits for password:"))
    random_password= generate_random_password(number)
    print(f"The password generated is:{random_password}")

except ValueError as e:
    print(f"Error:{e}, please enter a valid positive number")