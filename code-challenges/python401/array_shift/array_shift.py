# original_arr = input().split()
# original_val = input()

# def insertShiftArray(original_arr, original_val):
#     middle_position = len(original_arr) // 2 
#     if len(original_arr) % 2 == 0:
#         for i in range(middle_position):
#             new_arr.append(original_arr[i])
#         new_arr.append(original_val)
#     else:
#         for i in range(middle_position + 1):
#             new_arr[i] = original_arr[i]
        
#     print(new_arr)
#     for i in range(len(new_arr), len(original_arr)+1):
#         print('in the loop')
#         new_arr.append(original_arr[i-1])
#     return(new_arr)




def insertShiftArray(original_arr, original_val):
    new_arr = []
    middle_position = len(original_arr) // 2 
    if len(original_arr) % 2 == 0:
        for i in range(middle_position):
            new_arr.append(original_arr[i])
    else:
        for i in range(middle_position + 1):
            new_arr.append(original_arr[i])

    new_arr.append(original_val)

    for i in range(len(new_arr), len(original_arr)+1):
        new_arr.append(original_arr[i-1])
    return(new_arr)