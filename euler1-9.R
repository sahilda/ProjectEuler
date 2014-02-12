## problem 1
max <- 1000000
max <- max - 1
a <- floor(max/3)
b <- floor(max/5)
c <- floor(max/15)
threecount <- vector()
fivecount <- vector()
sum <- 0

for(i in 1:a) {
  threecount <- c(threecount,3*i)
  if(5*i<max) {fivecount <- c(fivecount,5*i)}
  sum <- c(threecount,fivecount)
  sum <- sum[!duplicated(sum)]
  sum <- sum(sum)
  }
sum
#Optimal Solution

sumb <- 3*1/2*a*(a+1) + 5*1/2*b*(b+1) - 15*1/2*c*(c+1)
sumb

## problem 2

a <- 1
b <- 2
add <- 2
max <- 3999999

for (i in 1:50) {
a <- a + b
if (a > max) {print('stop'); break()}
if (a %% 2 == 0) {add <- sum(add,a)}
b <- a + b
if (b > max) {print('stop'); break()}
if (b %% 2 == 0) {add <- sum(add,b)}
}
add

## Problem 3
a <- proc.time()
max <- 600851475143
count <- 7000
primes <- 2

isprime <- function(x) {
  prime <- 99
  for (i in 2:(x-1)) {
    if (x %% i == 0) {prime <- 0; break()} 
  } 
  if (prime == 0) {return(prime)} else {prime <- 1; return(prime)}
}

for (i in 3:count) {
  if (isprime(i) == 1) primes <- c(primes,i)
}

for (i in 1:length(primes)){
  while (max %% primes[i] == 0) {max <- max/primes[i]}
    if (max == 1) {print(primes[i]); break()}
  }

proc.time() - a

## problem 4
ispalin <- function(x) {
  strReverse <- function(x) {sapply(lapply(strsplit(x, NULL), rev), paste,collapse="")}
  if(nchar(x) == 6) {
    if(substr(x,0,3) == strReverse(substr(x,4,6))) return(1)
    else return(0) }
  else {
    if(substr(x,0,2) == strReverse(substr(x,4,5))) return(1)
    else return(0) }
}

for(i in 999:900) {
  for(j in 999:900) {
    prod <- ispalin(j*i)
    if (prod == 1) {break()}
  }
  if (prod == 1) {print(i) ; print(j); print(j*i) ; break()}
}

## Problem 5
"Necessary numbers from 1-20 needed at least: 
20 19 18 17 16 15 14 13 12 11"

nums <- c(60,19,18,17,16,14,13,11)

for (i in 1396755360) {
  counter <- vector()
  for (j in 1:length(nums)) {
    if (i %% nums[j] == 0) counter[j] <- 1 else counter[j] <- 0
  }
  if (sum(counter) == 10) {
    print(i) 
    break()
  }
}

## problem 6
max = 100
sumsquares <- 0
squaresums <- 0
for (i in 1:max) {
  sumsquares = sumsquares + i^2
  squaresums = squaresums + i
}
squaresums ^ 2 - sumsquares

## problem 7
count <- 70000000
primes <- c(2,3,5,7)

isprime <- function(x) {
  prime <- 99
  if (x %% 2 == 0) {prime <- 0; return(prime)}
  sequence <- seq(3,sqrt(x),2)
  for (i in sequence) {
    if (x %% i == 0) {prime <- 0; break()} 
  } 
  if (prime == 0) {return(prime)} else {prime <- 1; return(prime)}
}

for (i in 11:count) {
  if (isprime(i) == 1) primes <- c(primes,i)
  if(length(primes) == 100000) {print(primes[length(primes)]);break()}
}


## Problem 8 - finding the max product of consequtive numbers in a 1000 digit number
number <- as.character("7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")

max <- 0
prods <- function(num) {
  counts <- vector()
  for (i in 1:nchar(num)) {
    counts <- as.numeric(c(counts,substr(num,i,i)))        
  }
  return(prod(counts))
}

for (i in 1:nchar(number)){
  digits <- substr(number,i,i+4)
  current <- prods(digits)
  if (current > max) {
    max <- current
    counter <- i
  }      
}
max
counter
substr(number,counter,counter+4)

## Problem 9
# a < b < c
# a^2 + b^2 = c^2
# a + b + c

maxa = 331; maxb = 499

for (b in 1:maxb) {
  for(a in 1:maxa) {
    c <- 1000 - a - b
    aabb <- a*a + b*b
    cc <- c*c
    if (aabb == cc) break()
  }
  if (aabb == cc) {print(paste(a,b,c));print(prod(a,b,c));break()}
}



