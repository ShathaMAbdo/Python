
import os


file = open("helloworld.txt","w")  #creating a text file with the command function "w"
L = ["This is my first file in Linux and I am editing it in Vim! \n"]
file.write("Hello World! \n")
file.writelines(L)
file.close()                   # Use the close() to change file access modes

f = open("helloworld.txt", "r")   #('r’) opens the text files for reading only
print(f.read())                #The "f.read" prints out the data in the text file in the shell when run.


os.chdir('C:\\Python33') # change directory
print(os.getcwd())