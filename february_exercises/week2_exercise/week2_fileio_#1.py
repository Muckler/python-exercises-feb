#Must have a file in folder that is text to read
userin = input('Enter a file name..  ')
file_handle = open(userin, 'r')
contents = file_handle.read()
file_handle.close()
print(contents)
