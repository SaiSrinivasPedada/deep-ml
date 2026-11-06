import numpy as np

import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    length = len(data)
    if length == 0:
        return {}  # Return an empty dictionary or raise a ValueError if preferred
    
    data_mean = np.mean(data)
    data_median = np.median(data)
    
    # Correct mode calculation: find the unique values, count them, and map back
    vals, counts = np.unique(data, return_counts=True)
    data_mode = vals[np.argmax(counts)]
    
    data_variance = np.var(data)
    data_std = np.std(data)
    data_25th_per = np.percentile(data, 25)
    data_50th_per = np.percentile(data, 50)
    data_75th_per = np.percentile(data, 75)
    
    # Corrected IQR calculation (using proper variable names and subtraction)
    data_iq_range = data_75th_per - data_25th_per
    
    return {
        'mean': data_mean, 
        'median': data_median, 
        'mode': data_mode, 
        'variance': data_variance, 
        'standard_deviation': data_std, 
        '25th_percentile': data_25th_per, 
        '50th_percentile': data_50th_per, 
        '75th_percentile': data_75th_per, 
        'interquartile_range': data_iq_range
    }