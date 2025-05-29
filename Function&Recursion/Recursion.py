# Recursion are the tpe of code that help to perfrom the task better than loop in some condition

# recursion are the another type way to wirte the loop, the program that can be solved by loop is also solved by recursion.


def show(n=1):
    if n >= 1:  
        print(n)
        show(n-1)
        
show(5)
