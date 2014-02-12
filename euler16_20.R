#Euler 16 and 20

#!/bin/etc R
library('Rmpfr')
options(scipen=999)
x <- as.character(2^1000)
x <- factorial(100)

sum_of_digits <- function(x){
	sum = 0
	for(i in 1:nchar(x)){
		sum = sum + as.numeric(substring(x,i,i))
	}
	return(sum)
}

x = 1:20
samp = list()
samp$a <- x
samp$b <- 2^x

for(i in 1:20){
samp$c[i] <- sum_of_digits(samp$b[i])
}

matrix(samp$b,ncol=10,byrow=T)

x <- mpfr(2,1000)
x <- x^1000

#####In Python
x = pow(2,1000)
sum = 0
for num in str(x):
	sum += int(num)

sum(int(digit) for digit in str(math.factorial(100)))
