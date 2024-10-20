sourceFile = input("Enter the name of the source file: ")
copyFile = input("Enter the name of the copied file: ")
with open(sourceFile, 'r')as src:
    content = src.read()
with open(copyFile, 'w')as dest:
    dest.write(content)
print("Contents of: ", sourceFile, "are now copied to", copyFile)
