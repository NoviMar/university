def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def can_win(N):
    result = [None] * (N + 1)
    result[1] = True

    for i in range(2, N + 1):
        if is_prime(i) and i != N:
            continue

        result[i] = 0

        for j in range(1, 4):
           if i>j and result[i - j] == 0:
              result[i] = 1
              break
    
    return result[N]

N = int(input('Введите число спичек: '))
if N > 0:
    if can_win(N) == 1:
        print('Начинающий игрок имеет выигрышную стратегию.')
    else:
        print('Второй игрок имеет выигрышную стратегию.')
else:
    print('Некорректные входные значения.')
