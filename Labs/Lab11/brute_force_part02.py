number_list = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

# Place your linear_search() developed in part 1 below:
def linear_search(search_list, target_value):
    for index in range(len(search_list)):
        print(search_list[index])
        if search_list[index] == target_value:
            return index

    raise ValueError(f'{target_value} not in list')

try:
# Call the function below...
    linear_search(number_list, target_number)
    print("Found {0} in the list!".format(target_number))
except ValueError as error_message:
    print("{0}".format(error_message))