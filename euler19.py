day_of_week = ['sun','mon','tues','wed','thur','fri','sat']
month = range(1,13)
days_in_year = 365
current_year = 0
current_day = 0

while current_year < 10:
	current_day += 1
	current_day_of_week = day_of_week[current_day % 7]


	if current_day == 365:
		current_year += 1
		current_day = 0