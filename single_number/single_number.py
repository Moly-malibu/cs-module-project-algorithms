'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

def single_number(arr):
    fool = []
    for x in arr:  
      if x not in fool:  
        fool.append(x) #add 
      else:
        fool.remove(x)  
    return fool[0]  

def single_number_best(arr):
  count = {}
  for x in arr:
    if x in count:
      count[x] += 1
    else:
      count[x] = 1
  for key in count:
    if count[key] == 1:
      return key

arr = []

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2]

    print(f"The odd-number-out is {single_number(arr)}")