def upper_bound(arr, elementToSearch):
    firstIndex = -1
    lastIndex = len(arr)
    while lastIndex > firstIndex + 1:
        middleIndex = (lastIndex + firstIndex) // 2
        if arr[middleIndex] > elementToSearch:
            lenastIndex = middleIndex
        else:
            firstIndex = middleIndex
    return lastIndex

def print_result(arr, elementToSearch, index):
    if index < len(arr) and arr[index] == elementToSearch:
        print(f"Элемент {elementToSearch} и имеет индекс: {index}")
    else:
        print(f"Элемент {elementToSearch} должен иметь индекс: ", index)

N = int(input('Введите размер массива: '))
print('Введите упорядоченно элементы массива, используя клавишу Enter')
arr = [int(input()) for i in range(N)]

elementToSearch = int(input('Введите ключ: '))
index = upper_bound(arr, elementToSearch)
print_result(arr, elementToSearch, index)