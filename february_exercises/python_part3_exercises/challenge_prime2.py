#not working yet
my_list = []
def is_factor(big_number):
  global my_list
  for i in range(1, big_number + 1):
    if big_number % i == 0:
      my_list.append(i)
  return (my_list)
#send my_list into prime_factor function

prime_list = []
def prime_factor(if_prime):
  for each in if_prime:
    for i in range(1, each):
      if each % i == 0:
        print("no prime factors")
      else:
        prime_list.append(each)   
  new_prime = []
  for num in prime_list:
    if num not in prime_list:
      new_prime.append(num) 
  return(new_prime)

is_factor(687)
print(my_list)

prime_factor(my_list)
print(prime_list)
