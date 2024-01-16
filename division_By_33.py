num = int(input('Введите число: '))
sum_1, sum_2 = 0, 0

def division(num, sum_1, sum_2):
    if num == 0:
        if sum_1 % 3 == 0 and sum_2 % 11 == 0:
            return 'YES'
        else:
            return 'NO'    
    else:
        two_last_digit = num % 100
        sum_2 += two_last_digit
        sum_1 = sum_1 + two_last_digit % 10 + two_last_digit//10
        num //= 100
        return division(num, sum_1, sum_2)
    
result = division(num, sum_1, sum_2)
print(result) 