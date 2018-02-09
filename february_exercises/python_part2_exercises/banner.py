banner = input('Please input your message for the banner... ')
my_list = []
my_list.append("*" * len(banner) + "****")
my_list.append("*" * len(banner) + "****")
my_list.insert(1, "* " + banner + " *")
  
for i in range(0, 3):
  print(my_list[i])

