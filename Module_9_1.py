def apply_all_func(int_list : (list), *functions):
    results = {}
    function = functions
    for i in function:
        result = i(int_list)
        results[i.__name__] = result
    print(results)


apply_all_func([6, 20, 15, 9], max, min)
apply_all_func([6, 20, 15, 9], len, sum, sorted)
