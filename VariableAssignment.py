a = 10
print ("value of a is :" , a)
print ("Type of a is :", type(a))
b=15.25
c = a + b
print(c)

msg = "Hello Jigar..!!!"
print (msg)

msg_str = 'string can be within single qoutes'
print (msg_str)

print("This is for including new line ")
print("Hello \n World")
print("This is for including tab  ")
print("Hello \t World")
print ("len () function is used for getting the length of the string")
# Hash is used for commenting 
print("length of string jigar is :", len("jigar"))

#string functions in python  indexing 
mystr = "Hello World"
print ("Char at 0 index is :",mystr[0])
# there can also b negative indexing in python 

print ("Character l using negative index -2  :", mystr[-2])

#Substring or string slicing in python 
print ("string slicing syntax mystr[2:4] :",mystr[2:4])

#Substring or string slicing in python 
print ("string slicing from index 2  till end mystr[2:] :",mystr[2:])

#Substring or string slicing in python 
print ("string slicing from 0  till 3 index end mystr[:3] :",mystr[:3])


#Substring or string slicing in python 
print ("string slicing from 3 to till 6 mystr[3:6] :",mystr[3:6])

#Substring or string slicing in python 
print ("string slicing using step size of 2  mystr[::2] :",mystr[::2])

#Substring or string slicing in python 
print ("string slicing using negative index  mystr[::-1]  basically used for reserving string :",mystr[::-1])

#string operations 

print("jigar * 10 =",msg * 10)


print("Printing in uppercase : ", msg.upper())
print("Printing in lowercase : ", msg.lower())

print("This is split function : ", msg.split())

x = "hi this is a string "

print("split with specific letter", x.split('i'))