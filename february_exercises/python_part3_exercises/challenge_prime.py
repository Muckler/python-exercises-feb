my_list = []
def is_factor(big_number):
  global my_list
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

print (is_factor(100001))

prime_factor(my_list)
print(prime_list)
