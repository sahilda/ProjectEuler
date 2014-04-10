function fib_even_sum(num) {
	num1 = 1;
	num2 = 2;
	sum = 0;

	while (num1 < num || num2 < num) {
		if(is_even(num1) && num1 < num) {sum += num1;}
		if(is_even(num2) && num2 < num) {sum += num2;}
		num1 = num1 + num2;
		num2 = num1 + num2;
	}

	return sum;
}

function is_even(num) {
	return(num%2 == 0);
}

console.log(fib_even_sum(4000000));
//4613732