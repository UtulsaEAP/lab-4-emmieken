"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Emmie Kennemer
Lab Time: 2/22/24
"""

def password_mod():
    password = input()
    
    for i in password:
        if i == "i":
            password += "1"
        elif i == "a":
            password += "@"
        elif i == "m":
            password += "M"
        elif i == "B":
            password += "8"
        elif i == "s":
            password += "$"
        else:
            password += i
        
    
    print(str(password) + "!")

if __name__ == "__main__":
    password_mod()