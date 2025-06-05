# f = open("/workspaces/LearningPython/I/O Learning/hello.txt", "a")

# data = f.write("i m learning python today")

# f.close()


# now reading the content for files can be done by two methods.

# 1.  data = f.read()
# 2.  dta  = f.readline()


# f = open("/workspaces/LearningPython/I/O Learning/hello.txt" , "r")
# data = f.read()

# print(data)
# f.close()



# f = open("/workspaces/LearningPython/I/O Learning/hello.txt" , "r")
# data = f.readline()
# print(data, end = "")

# data1 = f.readline()
# print(data1, end = "")

# data2 = f.readline()
# print(data2)


# f.close()


# f= open("/workspaces/LearningPython/I/O Learning/hello.txt" , "a")
# data = f.write("Hello dear yes i m sure you learn python and DSA")

# f.close()



# with syntax 
# with open("demo.txt" , "a") as f:
    #  data = f.read()

# with open("/workspaces/LearningPython/I/O Learning/hello.txt" , "r") as f:
#     data = f.read()
#     print(data)

# with open("/workspaces/LearningPython/I/O Learning/hello.txt" , "w") as f:
#     data = f.write("Hello")
#     print(data)


# Deleting a file: using OS Module

# Module (like code library) is a file written by another programer that generally as a function we can use.

# import os
# os.remove(filename)

# We can download the package by giving comand : " pip install (module name) "

# import os

# os.remove("/workspaces/LearningPython/I/O Learning/helo.txt")


# with open("/workspaces/LearningPython/I/O Learning/hell.txt" , "r") as f:
#     data = f.read()
#     newData = data.replace("java","Python")
#     print(newData)

# with open("/workspaces/LearningPython/I/O Learning/hell.txt" , "w") as f:
    
#     data =f.write(newData)

# word ="learning"
# with open("/workspaces/LearningPython/I/O Learning/hell.txt","r") as f:
#     data = f.read()
#     if data.find(word) != -1:
#         print("Found")
#     else:
#         print("Not Found")



count = 0

with open("/workspaces/LearningPython/I/O Learning/i/number.txt" ,"r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for value in nums:
        if int(value)%2 == 0:
            count+=1

print(count)
    

    


    
