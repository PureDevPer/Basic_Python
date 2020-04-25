# Open a text file when there doesn't exist the file
try:
    f = open("none.txt", "r")
except IOError:
    print("Open a text file as a read mode")
    f = open("none.txt", "w")

