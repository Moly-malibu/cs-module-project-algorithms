'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    alter_arr = [number for number in arr if number !=0]
    zero = [number for number in arr if number is 0]
    alter_arr.extend(zero)
    return alter_arr

print(moving_zeroes([0, 3, 1, 0,-2]))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")