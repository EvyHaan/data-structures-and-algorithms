input_list = [str(s) for s in input().split()]
result = []

def reverse_array(lst):
  for elem in input_list[::-1]:
    result.append(elem)
    print(elem)

reverse_array(input_list)

print(result)