def binary_search(array, target):
    left, right = -1, len(array)

    while right - left > 1:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            left = middle
        elif target < array[middle]:
            right = middle

    return -1