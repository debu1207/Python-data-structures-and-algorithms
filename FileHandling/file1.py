"""
read and write files in the system
input image
out compressed image
"""

file = open('test.txt')
content = file.read()
file.seek(0)
print(file.readline())

# readlines method gives an array of lines of the file
print(file.readlines())

file.close()
