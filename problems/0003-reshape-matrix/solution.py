def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    if not a or not a[0]:
        return []
        
    first_row_len = len(a[0])
    
    # 1. Check if any row has a different length (ragged matrix check)
    if any(len(row) != first_row_len for row in a):
        return []

    # 2. Flatten the input matrix
    flat_list = [item for sublist in a for item in sublist]
    
    # 3. Unpack the new dimensions (rows, cols)
    rows, cols = new_shape
    
    # 4. If elements don't match the new shape, return [] instead of crashing
    if len(flat_list) != rows * cols:
        return []
    
    # 5. Slice the flat list into chunks of size 'cols' for each 'row'
    return [flat_list[i * cols:(i + 1) * cols] for i in range(rows)]