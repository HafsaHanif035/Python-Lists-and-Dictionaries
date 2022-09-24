# Task 01

list1 = []    #create a list
n=int(input("Enter number of objects of first list : "))      #getting input from user i.e, the elements of first list
for i in range(n):
    value= int(input("Enter a value : "))
    list1.append(value)
    
list2 = []  # create another list
n=int(input("Enter number of objects of second list : "))     #getting input from user i.e, the elements of second list
for i in range(n):
    value= int(input("Enter a value : "))
    list2.append(value)

list3=(list1+list2)     #merge elements of both lists
print("Merging list in an unsorted order:")
print(list3)

list3=sorted(list3)     #sort the elements of list which are stored in list3
print("Printing list in sorted form : "+str(list3))


# Task 02

list1 = []
n=int(input("Enter number of objects of first list : "))
for i in range(n):
    value= int(input("Enter a value : "))
    list1.append(value)
    
list2 = []
n=int(input("Enter number of objects of second list : "))
for i in range(n):
    value= int(input("Enter a value : "))
    list2.append(value)

list3=(list1+list2)
print(list3)
print("The largest number in the list is : " +str(max(list3)))     #printing the maximum number from list3 by using max() function
print("The smallest number in the list is : " +str(min(list3)))    #printing the minimum number from list3 by using min() function


# Task 03

from math import *          #importing all the 'math' libraries so that our code will consider trignometric functions
x= float(input("Enter value of x"))    
h= float(input("Enter value of h"))
m= {sin(x+h) - sin{x} }/h
n= cos(x)
print(m)
print(n)
if(m==n):
    print("Equal")
else:
    print("Not equal")


# Task 04

sample= {("Ayesha"):"16-December-2001", ("Hania"):"15-Feburary-2010", ("Tooba"): "11-August-2002",}    #create a dictinory named sample which contains all the data
print("Welcome to the birthday dictionary. We know the birthday's of: \nHania \nTooba\nAyesha")
name = input("\nWho's birthday do you want to look up?")
searchTuple = (name)                   # searchTuple gives that specific attribute which we want to search about
print(name+"'s birthday is "+sample[searchTuple])


# Task 05

sample_dict ={"name": "Kelly", "age":25 , "salary": 8000, "city": "New York"}    #creating dictionary
res = {key: sample_dict[key] for key in sample_dict.keys()              # This gives us that specific things which we want to get from the dictionary i.e, in this
       & {'name', 'salary'}}                          # case we only need name and salary
print(str(res))     # print result

      
         


