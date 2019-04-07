def simpleSort(arr):
    n = len(arr)
    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                salto = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = salto
            j += 1
    return arr

if __name__ == "__main__":
    arr = [8,6,5,3,1,11,22]
    print(simpleSort(arr))