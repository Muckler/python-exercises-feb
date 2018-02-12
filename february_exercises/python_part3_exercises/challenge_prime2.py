#not working yet
# import ar ange generator that allows going 
# from n to square root of n
from itertools import count, islice
from math import sqrt

def is_factor(big_number):
  my_list = []
  for i in range(1, big_number + 1):
    if big_number % i == 0:
      my_list.append(i)
  return (my_list)
#send my_list into prime_factor function

prime_list = []
def prime_factor(if_prime):
  x = True
  
  prime_list = [0]
  for each in if_prime:
    if each < 2:
      continue
    #using square root as the range bc half of factors 
    #will be <= to the square root of each and include
    #all the other factors > square root of each
    #islice does a range type function starting at
    #2 and does not use memory like range function
    for number in islice(count(2), int(sqrt(each)-1)):
      if not each % number:
        continue
      else:
        prime_list.append(each) 
  return(prime_list)

factor_list = is_factor(600851475143)
print(factor_list)

print(prime_factor(factor_list))

