def count_common_unique(list1, list2):
    
    #remove non string characters from the list
    clean_list_1 = [item for item in list1 if isinstance(item, str)]
    clean_list_2 = [item for item in list2 if isinstance(item, str)]
    
    #check for the length of list 1 and remove duplicate words 
    unique_strings_1 = [x for x in clean_list_1 if clean_list_1.count(x) == 1]
    unique_strings_2 = [x for x in clean_list_2 if clean_list_2.count(x) == 1] 

    #check for duplicate strings in both the list
    duplicates = list(set(unique_strings_1) & set(unique_strings_2))
    return len(duplicates)