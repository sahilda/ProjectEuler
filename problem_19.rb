def leapYear year 
	if year % 100 == 0 
		if year % 400 == 0
			return true
		end
	else
		return year % 4 == 0
	end
	false
end

def monthDays year
	days = {}
	days[1] = 31
	if leapYear(year) == true
		days[2] = 29
	else
		days[2] = 28
	end
	days[3] = 31
	days[4] = 30
	days[5] = 31
	days[6] = 30
	days[7] = 31
	days[8] = 31
	days[9] = 30
	days[10] = 31
	days[11] = 30
	days[12] = 31

	days
end

def countSundays startYear, endYear, startDay
	curYear = startYear
	curDay = startDay #0 is sunday, 7 is saturday
  sundayCounter = 0
  
  while curYear < endYear
    calenday = monthDays(curYear)
    calenday.each do |month, days|
      day = 1
      while day <= days
        if day == 1 && curDay == 0 #sunday being the first day of the month
          sundayCounter += 1
        end
        day += 1
        curDay = (curDay+1) % 7
      end
    end
    curYear += 1
  end
  sundayCounter
end

puts countSundays 1901, 2001, 2