import time

## function to determine number of factors
def num_of_factors(x):
	half = x/2 + 1
	num_factors = 1
	factors = []
	for i in range(1,half):
		if x % i == 0: 
			num_factors += 1
			factors.append(i)
	factors.append(x)
	return num_factors, factors

## function to produce triangle numbers, with memory input
def triangle_nums(x,prev=None):
	nat_num = 0
	if prev == None:
		for i in range(0,x+1):
			nat_num += i
	else:
		nat_num = prev + x
	return nat_num

def main():
	start = time.time()
	total = 0
	counter = 1
	marker = 0
	x = 0

	while(total < 500):
		x = triangle_nums(counter, x)
		counter += 1

		## optimization
		if x % 10 != 0: continue

		total, factors = num_of_factors(x)

		## fun printing messages
		if total > 5 and marker == 0: print 'making progres...'; marker += 1; print x, total
		elif total > 50 and marker == 1: print '...'; marker += 1; print x, total
		elif total > 100 and marker == 2: print '...'; marker += 1; print x, total
		elif total > 200 and marker == 3: print '...'; marker += 1; print x, total
		elif total > 250 and marker == 4: print '...halfway...'; marker += 1; print x, total
		elif total > 325 and marker == 5: print '...'; marker += 1; print x, total
		elif total > 400 and marker == 6: print '...'; marker += 1; print x, total
		elif total > 450 and marker == 7: print '...almost there...'; marker += 1; print x, total

	print x, total, factors
	end = time.time() - start
	print end

if __name__ == "__main__":
	main()

