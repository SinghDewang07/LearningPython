#in this we start to learn Dictonary and sets

#so let's start with the dictonaries

#Dictonaries are used the data in the format of key and values.

#Dictonaries are unorded, mutuable and don't allow duplicates keys

info = {
    "name" : "Dewang",
    "age" :23,
    "phone" : 1234567890,
}

print(info)
print(type(info))
print(info["name"])
info["name"] = "jyoti"

print(info)


#here we can assigned new key and value by this way in the dictornaries
info["sex"] = "female"
print(info)


#In Dictonaires we can create the nested dictonaries

info = {
    "name" : "Dewang",
    "subjects" : {
        "psy" : 79,
        "maths" : 70,
        "chemistry" :89,
    }
}


print(info["subjects"])

#there are various method used in dictonaries as we used in list , tuples and string

#Let's start with .key(). it is used to print all the key in the dictonaries
print(info.keys())


# Now lets prints the length of dictonaries
print(len(info))


# we can convert the dictonaries into list and tuples by type casting
print(list(info.keys()))
print(len(list(info.keys())))


# we can also print all the values of the dictnories
print(info.values())

#we can also convert the value in the list
print(list(info.values()))
print(type(list(info.values())))


# we can also print the all the key values pairs of the dictonaries by using the methods .items()
print(type(info.items()))



# In dictonaries we can get the value of key by two method but both have different pros and corns like:

marks = {
    "psy" : 89,
    "chem" : "F",
    "math" : 100,
}


# Now we can access the value of keys from these both methods but while a professional way we have to go with second ways becuase:

#  -> In first way if the key is not present in dictonary it will show error and the line of code written below it does not works good
print(marks["chem"])
print("hello");


#-> now in this second way dictonoary have inbuild method to fetch the value of the key, if the key is not presesnt is will show None and other code below it works fine
print(marks.get("chm"))
print("hello") 


print(type(marks["chem"]))


# str = 23.43
# a = int(str)
# print(type(a))


student = {
    "place" : "delhi",
    "age" : 23
}



#to add the new key value pair in the. 

# student.update({"phone" : 2345})
# print(student.items())

# a= 23
# b ="23"
# if( a == int(b)):
#     print("True")
# else:
#     print("False")



