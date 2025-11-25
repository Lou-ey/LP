# import heap class
from max_heap import MaxHeap

# create a heapsort function
def heapsort(lst):
    # create an empty list
    sort = []

    # make an instance of MaxHeap
    max_heap = MaxHeap()

    for item in lst:
        # add values from lst to max_heap
        max_heap.add(item)
        # print the heap list
        print(max_heap.heap_list)

    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)

    print(max_heap.retrieve_max())
    print(max_heap.heapify_down())
    return sort

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print("Sorted List: ", sorted_list)