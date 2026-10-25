def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    first_number=0
    second_number=1
    if n==0:
        fibonacci_list =[]
        return fibonacci_list
    elif n==1:
        fibonacci_list =[]
        fibonacci_list.append(first_number)
        return fibonacci_list
    elif n==2:
        fibonacci_list =[]
        fibonacci_list.append(first_number)
        fibonacci_list.append(second_number)
        return fibonacci_list
    else:
        fibonacci_list =[]
        fibonacci_list.append(first_number)
        fibonacci_list.append(second_number)
        for i in range(2,n):
            last_two=fibonacci_list[-2:]
            total=sum(last_two)
            fibonacci_list.append(total)
        return fibonacci_list