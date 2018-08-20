#working with files in python 
myfile = open('myfile.txt')
print(myfile.read())
print("trying to read again after first read")
print(myfile.read())
#to set cursor value again to 0 index to read the file again
myfile.seek(0)
print("trying to read again after using seek(0) function")
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
filepath = "E:\\Python_Programing\\myfile.txt"
#myfile1 = open(filepath)
#print(myfile1.read())
print("open file using with statement and the advantage of this is we did not have to close the file")
with open(filepath) as lv_file:
    contents = lv_file.read()
    print(contents)
print ("different file modes  r,w,a,r+,w+")
with open(filepath,mode='a') as f:
    f.write("\nthis is fourth line")

with open(filepath,mode='a') as f:
    f.writelines("this is fifth line")