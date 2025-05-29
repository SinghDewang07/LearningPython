nums =[]
i = 1;
while i <=10:
    nums.append(i*i)
    i +=1


print(nums)

mytuple = tuple(nums)
print(type(mytuple))
print(mytuple)


mytupe = (10, 12, 14, 16, 18)
# print(mytuple[2])
i =0
a =16
while i <= len(mytupe)-1:
    if(a == mytupe[i]):
        print("found at index", i)
        break
    i+=1 



# Break : are used to terminate the lopp when encountered
# Countinue : terminate execution in the current iteration & continue exection the loop in the next iteration


#for loop : are used for sequential traversal in the list, tuple and string etc.


num = [1,4,9,16,25,36,49,64,81,100]
for value in num:
    print(value)

search = tuple(num)
print(search)

x = 81 
i=0
for val in search:
    if(val == 81):
      print("found" ,i)
    i+=1
else:
    print("End")


# Range() : Range functions returns a sequence of numbers, starting from 0 by default, and increments by
# 1 (by default), and stops before a specified number.
    
    # range(start?, stop, step?)

    # for i in range(1,101,1):
    #     print(i)

    # for i in range(100,0,-1):
    #     print(i)

    a =6
    for i in range(1,11,1):
        print(a ,"*", i,"=",a*i)



    # pass is a null statement that does nothing. It is used as a placeholder for future code.
    for i in range(5):
        pass

    print("Pass has worked")



# write a program to print the sum of first n nummber using while

# a = int(input("Enter the number: "))
# i = 0;

# while a >= 0:
#     i = i + a
#     a -= 1

# print(i)
    
#write a program to calculate the factorial of the given number :

a = int(input("Enter the number: "))
ans = 1;

for i in range(1,a+1,1):
    ans = ans*i;
    print(i)

print(ans)


