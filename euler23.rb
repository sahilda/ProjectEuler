def abundant_number?(num)
    divisors = [0]
    i = 1

    while (i <= num/2)
        if num % i == 0
            divisors << i
        end
        i += 1
    end

    if divisors.reduce(:+) > num
        return true
    end

    false
end

def abundant_number(num)
    nums = []
    i = 12
    while i < num
        if abundant_number?(i)
            nums << i
        end
        i += 1
    end
    nums
end

def non_abundant_sums(num)
    all_nums = (1..num).to_a
    abun_sums = []
    abun_nums = abundant_numbers(num)

    abun_nums.each_with_index do |abun_num1, idx1|
        abun_nums[idx1..-1].each do |abun_num2|

            if abun_num1 + abun_num2 > num
                break
            end

            if abun_sums.include?(abun_num1 + abun_num2) == false
                abun_sums << abun_num1 + abun_num2
            end
        end
    end

    all_nums.reduce(:+) - abun_sums.reduce(:+)

end

puts non_abundant_sums(28123)
