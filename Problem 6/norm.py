"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Emmie Kennemer
Lab Time: 2/23/24
"""

def norm():
    # Write your code here
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())

    num_list = [num1, num2, num3, num4, num5]
    
    for i in num_list:
        if i > num1:
            print(f'{num1:.2f}')
    
    

if __name__ == "__main__":
    norm()