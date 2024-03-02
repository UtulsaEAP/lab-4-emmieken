"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Emmie Kennemer
Lab Time: 2/23/24
"""

def norm():
    # Write your code here
    num = int(input())
    num_list = []
    
    for i in range(num):
        amount = (input())
        num_list.append(float(amount))
    largest = max(num_list)

    for i in num_list:
        new_num = i/largest
        print(f'{new_num:.2f}')

        
    
    

if __name__ == "__main__":
    norm()