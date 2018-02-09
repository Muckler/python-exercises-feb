my_list = []
def is_factor(big_number):
  for i in range(1, big_number + 1):
    if big_number % i == 0:
      my_list.append(i)
  return my_list
#send my_list into prime_factor function

prime_list = []
def prime_factor(if_prime):
  for each in if_prime:
    for i in range(0, len(if_prime)):
      if each % if_prime[i] == 0:
        return False
      else:
         prime_list.append(each)
         return(prime_list)

is_factor(100001)
print(my_list)
prime_factor(my_list)
print(prime_list)
largest = 0
k = 1
for each in prime_list[1:]:
  if each == prime_list[k]:
    k =+ 1
  elif each > prime_list[k - 1]:
    print(largest)
    k =+ 1
  else:
    k =+ 1
   

 