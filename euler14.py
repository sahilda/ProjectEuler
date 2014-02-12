def route(x):
	def next_num(x):
		if x % 2 == 0: 
			return x/2
		else:
			return (3*x + 1)

	counter = 1
	end = 1
	while x != end:
		x = next_num(x)
		counter += 1

	return counter


max = 0
max_num = 0

for num in range(999999,0,-2):

	current = route(num)
	if current > max:
		max = current
		max_num = num

	print num

print max_num, max

