def InsertionSort(mas):
    for i in range(len(mas)):
        j = i - 1
        key = mas[i]
        while mas[j] > key and j >= 0:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = key
    return mas
