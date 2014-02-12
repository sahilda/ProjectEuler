##One to one thousand Word letter counter
number_to_letter_count = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:11}
number_to_letter_word = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight", 9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100:"hundred",1000:"onethousand"};

def letter_count(x):
	letter_count = ""
	if x == 1000:
		return number_to_letter_word[1000] # For 1000s place (11)

	if x >= 100:
		letter_count += number_to_letter_word[(x/100)] # For which hundred
		letter_count += number_to_letter_word[100] # For the 100s place (7) 
		x = x % 100
		if x != 0: letter_count += "and" # For the word and which is required for all numbers greater than 10

	if x >= 20:
		letter_count += number_to_letter_word[(x/10)*10] # add the prefix for numbers > 20
		letter_count += number_to_letter_word[x%10] # add the singles digit letter count

	if x < 20 and x > 0:
		letter_count += number_to_letter_word[x]

	return letter_count

count = 0
x = 1000

for y in range(1,x+1):
	count += len(letter_count(y))

print count