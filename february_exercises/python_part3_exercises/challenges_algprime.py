known_primes = [2, 3]
def is_prime(n):
	total_primes = len(known_primes)
	for i in range(0,total_primes):
		if(n % known_primes[i] == 0):
			# NOT PRIME!!
			return False
		else:
			# it might be prime, it might not. 
			# Its just not divisible by this number
			continue
	  known_primes.append(n)
	return True
for i in range(1,100):
  is_prime(i)
print(known_primes)