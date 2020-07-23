'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

def single_number(arr):
    no_dups = []
    for x in arr:  
      if x not in no_dups:  
        no_dups.append(x) #add 
      else:
        no_dups.remove(x)  
    return no_dups[0]  


def single_number_best(nums):
  count = {}
  for num in nums:
    if num not in counts:
      count[num] = 1
    else:
      counts[num] += 1
  for key in count:
    if count[key] == 1:
      return key

arr = []

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2]

    print(f"The odd-number-out is {single_number(arr)}")