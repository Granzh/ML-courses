def my_very_cool_hash(lst):
    if not isinstance(lst, list):
        if isinstance(lst, (int, str)):
            return hash(lst)
        
    result = 0
    for item in lst:
        if isinstance(item, list):
            result = (result * 31 + my_very_cool_hash(item)) % (2**32)
        elif isinstance(item, (int, str)):
            result = (result * 31 + hash(item)) % (2**32)
            
    return result


test_list = [1, "hello", [2, 3, ["nested"]], 4]
print(my_very_cool_hash(test_list))

test_list2 = [1, "hello", [2, 3], 4] 
print(my_very_cool_hash(test_list2))