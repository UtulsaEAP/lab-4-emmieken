"""
Complete the following python code to reverse the string entered by the user.

Name: Emmie Kennemer
Lab Time: 2/22/24
"""

def reverse_string():
    phrase = str(input())

    while len(phrase) >=1 and phrase != "Done" and phrase != "done" and phrase != "d":
        print(phrase[::-1])
        phrase = str(input())
    pass

    

    

if __name__ == "__main__":
        reverse_string()        