print("hello Github")

#Learning about list

marks = [ 23,53,56,54,22,77,46,467,36,35.99]
print(marks)

marks[4] = "student"
print(marks)

# Important Points
# -> Slicing in python works same as in string
# -> In python list are mutable where string are in immutable
# list can store all type of data

# print(marks[0:3]) -> In this slicing from insex 0 to index(3-1 =2) is count.
# print(marks[-3:-1]). -> in this way index are -3 to (-1 -1 = -2) is count.

print(marks[:len(marks)])



# Methods of List are :-> 

# list.append this is used to add the element at the end of list.

# print(marks.append(2345)) -> This is not wokring because marks.append(2345) add 2345 in the list but return none " so the print method return none"

marks.append(299)
# print(marks) -> Now in this way it works

# .remove will used for remove the items from list but we need to provide the value
marks.remove("student")

#this method is used to sort the items in the ascedning order of array but list items must in same suitable type
marks.sort()
print(marks)

# marks.sort(reverse = True) means sort arry in descending order
marks.sort(reverse=True)
print(marks)

# .reverse as method name tell it reverse the items of the list

car = ["honda","mercedeze", "jaguar","bmw"]
car.reverse()
print(car)

# .insert is used to add the items in the list at specific position
car.insert(2,"bently")
print(car)