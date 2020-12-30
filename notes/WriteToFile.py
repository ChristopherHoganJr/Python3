### Open File Version 1 - Need to close file after
# Opens file as variable
#file = open('my_file.txt')
# Reads file saved to variable and saves to new variable
#contents = file.read()
#print(contents)
# Close the file to save resources
#file.close()

### Open File Version 2 - Do not need to close file after
## Opening file is default to 'r' read mode
## Opening file in 'w' means write or 'a' means append
with open('new_file.txt', 'w') as file:
    file.write("\nNew text.")