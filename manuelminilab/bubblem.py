

class manuelbubble:

    def bubble_sort(items):
        changes = passes = 0
        last = len(items)
        swapped = True

        while swapped:
            swapped = False
            passes += 1
            for j in range(1, last):
                if items[j - 1] > items[j]:
                    items[j], items[j - 1] = items[j - 1], items[j]  # Swap
                    changes += 1
                    swapped = True
                    last = j


        print(items)

    print("Bubble Sort")

    while True:
        print("Enter as many numbers as you want.\n choose a number between 0 and 9.\nremember to Leave a space between each one and hit enter")
        numbers = input()
        items = [int(num) for num in numbers.split() if num.isdigit()]
        if items: bubble_sort(items)