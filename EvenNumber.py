'''
This script prints all even numbers between 1 and 100
'''

# define your function here
def even_number():
    # loop from 1 to 100
    for i in range(1, 101):
        
        # if the number is even
        if i % 2==0:
            # print it
            print(i)
even_number()    