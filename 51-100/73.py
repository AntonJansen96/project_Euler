# 73 - COUNTING FRACTIONS IN A RANGE

# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
# it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 3 fractions between 1/3 and 1/2.

# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?

def gcd(a,b):
	while b != 0:
		a, b = b, a % b
	return a

limit = 12000
count = 0

for n in xrange(1, limit+1):
	for d in xrange(1, limit+1):
		f = n/float(d)
		if f > 1/3. and f < 1/2. and gcd(n,d) == 1:
			count += 1

print(count)
# solved, runs in 36s
