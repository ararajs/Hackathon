# [1,2,6,3,17,82,23,234] -> 26
#           Solution [3,6]
 
#           [1,2,6,3,17,82,23,234] -> 40
#           Solution [4,6]
 
#           [1,2,6,3,17,82,23,234] -> 23
#           Solution [6]
 
import timeit
arr = [1,2,6,3,17,82,23,234]


def sum_or_not(arr,x):
    def identifier(arr,x,outp = [],index = 0, sub_arr = []):
        if index == len(arr):
            if sum(sub_arr) == x:
                outp.append(sub_arr)
                return
        else:
            identifier(arr,x,outp,index+1, sub_arr)                
            identifier(arr,x,outp,index+1, sub_arr +[arr[index]])
        return outp    
    possbile_vals = identifier(arr,x)
    try:
        best_possbile_val = min(possbile_vals, key = len)
    except:
        return "No possible combination found"
    indices = []
    for values in best_possbile_val:
        for ind,arr_val in enumerate(arr):
            if (arr_val == values) and (ind not in indices):
                indices.append(ind)
                break
    return indices
    
print(sum_or_not(arr,260))
