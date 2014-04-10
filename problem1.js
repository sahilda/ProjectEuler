function multiple_3_5(num) {
	if(num % 3 == 0 || num % 5 == 0) {
		return(true);
	} else
	{
		return(false);
	}
}

function sum_of_multiples(num) {
	i = 1;
	sum = 0;
	while (i < num) {
		if (multiple_3_5(i) == true) {
			sum += i;
		}
		i += 1;
	}
	return(sum);
}

console.log(sum_of_multiples(1000));
//233168