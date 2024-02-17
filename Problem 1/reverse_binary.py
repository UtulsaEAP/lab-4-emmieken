"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Emmie Kennemer
Lab Time: 2/16/24

"""

def reverse_binary():
    user_num = int(input())

    while user_num > 0:
        user_num += 1    
        print(user_num % 2)
    


if __name__ == "__main__":
    reverse_binary()