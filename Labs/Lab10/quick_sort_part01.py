# Define your quicksort function
def quicksort(list, start, end):
    # Base case: If the list from start to end has 0 or 1 elements, it's already sorted
    if start > end:
        return
    print(list[start])
    start += 1
    quicksort(list, start, end)


colors = ["blue", "red", "green", "purple", "orange"]

quicksort(colors, 0, len(colors) - 1)

