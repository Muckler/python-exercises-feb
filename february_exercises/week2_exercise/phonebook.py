
phone_book = {
    'Mike': '867-5309'
}
i = 0
while i < 1:  
  print(" Electronic Phone Book\n",("=" * 21))
  print(" 1. Look up an entry\n","2. Set an entry\n","3. Delete an entry\n",
  "4. List all entries\n","5. Quit\n")
  pick = int(input('What do you want to do (1-5)?  '))
  if pick == 1: 
    name_search = phone_book.get(input('Enter name..'),'Not in phonebook')
    print(name_search)
  elif pick == 2: 
    phone_book.update({input('Enter name\n'): input('Enter phone number\n')}) 
  elif pick == 3: 
    del phone_book[input('Enter name to remove..')]
  elif pick == 4: 
    print(phone_book.items())
  elif pick == 5:
    i = 10




  
  


