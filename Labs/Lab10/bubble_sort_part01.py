nums = [5, 2, 9, 1, 5, 6]

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

swap(nums, 3, 5)
print(nums)