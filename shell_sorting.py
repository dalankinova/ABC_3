import timeit

def shell_sort_by_area(obj_list, reverse=False):
    start_time = timeit.default_timer()
    for i in range(len(obj_list)):
        j = i - 1 
        key = obj_list[i]
        while obj_list[j].get_area() < key.get_area() and j >= 0:
            obj_list[j + 1] = obj_list[j]
            j -= 1
        obj_list[j + 1] = key
    result_time = timeit.default_timer() - start_time
    if not reverse:
        return obj_list, result_time
    return obj_list[::-1], result_time