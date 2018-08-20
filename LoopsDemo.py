
#Demonstration of while loop in python 

i = 1 

while i < 6 :
    print (i)
    i += 1


print ("While loop with break statement")  
j = 1
while j < 6 :
    print (j)
    if j == 3 :
        break
    j += 1


print ("While loop with continue statement")  
k = 0
while k < 6 :
   k += 1
   if k == 3 :
        continue
   print (k)
    