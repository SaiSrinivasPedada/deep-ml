def add_two_numbers(l1, l2):
    # l1 and l2 are lists of digits in reverse order
    
    # 1. Use slicing [::-1] to get the normal order without returning None
    number_1 = int("".join(map(str, l1[::-1])))
    number_2 = int("".join(map(str, l2[::-1])))
    
    # 2. Add the integer values together
    sum_value = number_1 + number_2
    
    # 3. Convert back to string, map to int, and reverse again to match 
    # the input's reverse-order format
    revised_list = list(map(int, str(sum_value)))[::-1]
    
    return revised_list