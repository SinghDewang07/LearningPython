#Tuples are the same as list but they are immmutable data type, means we. can't chaneg the data of tuples

# tup = (1,)
# print(type(tup))
# print(tup)


# lis = [1]
# print(type(lis))
# print(lis)

# tup = (1,2,1,3,4,1,5,6,7,8,90)
# print(type(tup))
# print(tup)

# # tup.index(2) is used to return the index of first occurance of element 2 in the tuple
# print(tup.index(2))

# # tup.count return the 
# a = tup.count(1)
# print(a)


# This code help 
# favmov = []
# favmov.append(input("enter your favourite movie name"))
# favmov.append(input("enter your favourite movie name"))
# favmov.append(input("enter your favourite movie name"))


# print(favmov)


# Write a programe to know whether the list is palindrone or not

# let's take exomaple of abc -> cba is plaindone

# lis = [1,2,1]
# listCopy = lis.copy()
# listCopy.reverse()

# print(lis)
# print(listCopy)

# if(lis == listCopy):
#     print("plaindrome")
# else:
#     print("Not palindrome")



# lis = 1,2,2,4,1]
# listCopy = lis.copy()
# listCopy.reverse()

# print(listCopy)
# print(lis)

# a =lis
# print(lis)
# print(a)
# a.reverse()

# print(lis)
# print(a)

# print(a == lis)





# tup = (1,2,3,4,5,6,7,89,0)
# tup[2] = 23;
# print(tup)

# # Means tuples don't provide option to items assigment.


# Write a program to count the number of stuednt having grade A

# grade = ('A','B','D','A','B','D','A','B','D','A','B','D','A','B','D')
# print(grade.count('A'))

grade = ['A','B','D','A','B','D','A','B','D','A','B','D','A','B','D']
grade.sort()
print(grade)