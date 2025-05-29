# sets is collection of unorded items
# Each element in the set must ne unique and immutable

items = {1,2,3,4,5,6,7,"hello"}
print(items)
print(type(items))


# Duplicates element are not allowed in set even we code set automatic remove duplicay from the code

item = {1.2,2,3,3,3,4,4,4,-5,5,6,6,7,8,9,9,0,"-hello","world","hello"}
print(len(item))
print(item)

# we can create the empty set by this syntax

collection = set()
print(type(collection))


lis = []
print(type(lis))

tup = ()
print(type(tup))



#.add method is used to add the value in the set

collect = set()
print(type(collect))

collect.add(1)
collect.add(2)
collect.add("hello")
collect.add(1)

print(collect)
print(len(collect))

# collect.remove("hello")
# print(collect)

# collect.pop()
# collect.pop()
# collect.pop()

#we can used a method to directly remove all the data from the set
print(collect)

collect.clear()
print(collect)



# in sets we can make intersection and unions between sets.

hel = {1,2,3}
leh ={1,2,3,4,5,6}


# use to make set of both values
print(hel.union(leh))


#use to make set of commom values
print(hel.intersection(leh))


## Problem Solving
word_meaning = {
    "table" : ["a piece of furnitur", " list of facts & figue"],
    "cat" : "a foure leg animal"
}

print(word_meaning.keys())