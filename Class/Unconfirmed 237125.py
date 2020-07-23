def single_number(nums): # O(n)
    counts = {}
    # iterate through nums
    for num in nums: # O(n)
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    for k, v in counts.items(): # O(n)
        if v == 1:
            return k