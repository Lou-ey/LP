# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

# Place your linear_search() developed in part 1 below:
def linear_search(search_list, target_value):
    matches = []
    for index in range(len(search_list)):
        print(search_list[index])
        if search_list[index] == target_value:
            matches.append(index)
    if matches:
        return matches
    else:
        raise ValueError(f'{target_value} not in list')

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
