def find_largest_elem(arr):
    # Pick a seed number
    largest = arr[0]
    for item in arr:
        if item >= largest:
            largest = item
    return largest

def create_largest_list(arr,output_list=None):
    output_list = []
    while arr:
        largest_found = find_largest_elem(arr)
        output_list.append(largest_found)
        arr.remove(largest_found)
    return output_list
