def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

no1 = int(input("Enter a number: "))
no2 = int(input("Enter a number: "))
no3 = int(input("Enter a number: "))
no4 = int(input("Enter a number: "))
no5 = int(input("Enter a number: "))

arr = [no1, no2, no3, no4, no5]

bubblesort(arr)

print("Sorted list is: ")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")