function is_prime(num) {
    largest_pos = Math.sqrt(num);
	i = 2;
	while (i <= largest_pos) {
		if(num % i == 0) {
			return(false);
		}
		i += 1;
	}
	return(true);
}

function largest_prime_factor(num) {
	j = 2;
	largest_prime = 1;
	largest_num = Math.sqrt(num);
	while (j < largest_num) {
		while(num % j == 0) {
			num = num / j;
			if(is_prime(j)) {largest_prime = j;}
		}
		j += 1;
	}
	return(largest_prime);
}

console.log(largest_prime_factor(600851475143));
//6857