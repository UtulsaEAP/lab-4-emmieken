"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Emmie Kennemer 
Lab Time: 2/22/24
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    # YOUR CODE HERE

    combined_x_value = a + d   # 5 + 4 = 9
    combined_y_value = b + e   # 2+2 = 4
    total_sum = c + f          #3 + 9 = 12 
    t=0
    for x in range(-10, 10):
        for y in range (-10, 10):
            if combined_x_value*x + combined_y_value*y == total_sum:
                print(f"x = {x} , y = {y}")
                t =1
        if t ==1:
            break
    if t==0:
        print("There is no solution")
    
if __name__ == "__main__":
    brute_eq()