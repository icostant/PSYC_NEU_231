
# Defines x and y from given list of 2 values (or the first 2 values of a list). 
# If x and y are integers, passes values to if statement
# If/elif statements sort and return higher value first
def sort_numbers_low_high_2 (list):
    x = list[0]
    y = list[1]
    
    if type(list[0]) is int and type(list[0]) is int:
        if x > y:
            print (x, y)
        elif x < y:
            print (y, x)
        elif x == y:
            print (x, "=", y)
    else:
        print("Sorry, please give me an integer.")
        
# Determines if all list values are integers, passes values if yes. Breaks if no
# Sort list, return and print from higher value to lower
def sort_numbers_low_high_many (list):
    for i in list:
        if type(i) is int:
            continue
        else:
            print ("There are non-integer values in your list.")
            break

    return(sorted(list, reverse=True))
    print(sorted(list, reverse=True))
    
# For each member of the array up to size n, each array value is interatively
# multipled. 
def multiply_array (list):
    result = 1
    n = len(list)
    for i in range(0,n):
        result = result * list[i]
    return result
    print(result)

        
    