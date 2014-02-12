
# Hardpath method
"""
def possible_moves(x,y,max):
	moves = ''
	if x < max: moves += 'x'
	if y < max: moves += 'y'
	return moves

def point(x,y,max):
	return {'x':x,'y':y,'move':possible_moves(x,y,max)}

def print_point(point):
	print point['x'], point['y'], point['move']

def paths(start,max):
	if start['move'] == '' or start['move'] == 'x' or start['move'] == 'y':
		count.append(1)
	if start['move'] == 'xy':
		paths(point(start['x']+1,start['y'],max),max)
		paths(point(start['x'],start['y']+1,max),max)

count = []
paths(point(0,0,4),4)
print sum(count)

def hard_calc(x,y):
	if x == 0 or y == 0:
		return 1
	elif x == 0 or y == 1:
		return x + y
	else:
		return hard_calc(x-1,y) + hard_calc(x,y-1)

"""

# Calculation Method

def make_first_row(x):
	row = []
	for i in range(0,x):
		row.append(1)
	return row

def make_next_row(row_num,last_row):
	row = []
	start = last_row[1] * 2
	row.append(start)

	for i in range(0,len(last_row)-2):
		row.append(row[i]+last_row[i + 2])

	return row


def print_rows(x):
	row = make_first_row(x+1)
	print row
	for i in range(2,x+2):
		row = make_next_row(2,row)
		print row

print_rows(20)