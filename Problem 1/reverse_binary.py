"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Emmie Kennemer
Lab Time: 2/16/24

"""

def reverse_binary():
    user_num = int(input())

    while user_num > 0:  
        print(user_num % 2)
        user_num = user_num/2

    
    #As long as x is greater than 0
    #Output x modulo 2 (remainder is either 0 or 1)
    #Assign x with x divided by 2
    


if __name__ == "__main__":
    reverse_binary()