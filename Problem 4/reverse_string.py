"""
Complete the following python code to reverse the string entered by the user.

Name: Emmie Kennemer
Lab Time: 2/22/24
"""

def reverse_string():
    phrase1 = str(input())
    phrase2 = str(input())

    for i in range(len(phrase1) -1, 0-1, -1):
        print(phrase1[i], end = "")
    
    for i in range(len(phrase2) -1, 0-1, -1):
        print(phrase2[i], end = "")



if __name__ == "__main__":
        reverse_string()        