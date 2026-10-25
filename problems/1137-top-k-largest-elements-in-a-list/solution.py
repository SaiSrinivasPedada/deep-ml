def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    if values == [] or len(values)<=2:
        revised_list = sorted(values, reverse=True)
    else : 
        revised_list=[]
        maximum_1=max(values)
        revised_list.append(maximum_1)
        values.remove(maximum_1)
        maximum_2=max(values)
        revised_list.append(maximum_2)
        values.remove(maximum_2)
        maximum_3=max(values)
        revised_list.append(maximum_3)    
    return revised_list