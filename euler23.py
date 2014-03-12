# Incomplete - look at ruby solution

def abundant_number(num):
    divisors = [0]
    i = 1

    while (i <= num/2):
        if num % i == 0:
            divisors.append(i)
        i += 1

    if sum(divisors) > num:
        return True

    return False

def abundant_numbers(num):
    nums = []
    i = 12
    while i < num:
        if abundant_number(i):
            nums.append(i)
        i += 1
    return nums

def non_abundant_sums(num):
    all_nums = range(1,num+1)
    print 'all numbers arrayed..'
    abun_sums = []
    abun_nums1 = abundant_numbers(num)
    abun_nums2 = abun_nums1
    print 'all abundant numbers arrayed..'

    for abun_num1 in abun_nums1:
        for abun_num2 in abun_nums2:
            if (abun_num2 + abun_num1) < num and ((abun_num1 + abun_num2) not in abun_sums): abun_sums.append(abun_num1 + abun_num2)
        abun_nums2.remove(abun_num1)

    return sum(all_nums) - sum(abun_sums)

print non_abundant_sums(28123)
