def rotate_right_brute_force(arr, k):
    n = len(arr)
    k = k % n
    for _ in range(k):
        last = arr[-1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
    return arr


def rotate_right_optimized(arr, k):
    n = len(arr)
    k = k % n

    # Reverse helper function
    def reverse(sub_arr, start, end):
        while start < end:
            sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
            start += 1
            end -= 1

    reverse(arr, 0, n - 1)      # Reverse the whole array
    reverse(arr, 0, k - 1)      # Reverse the first k elements
    reverse(arr, k, n - 1)      # Reverse the remaining

    return arr


# Test
arr = [2, 7, 11, 15, 3]
k = 3

print("Original array:", arr)

# Uncomment to test brute force
# rotated = rotate_right_brute_force(arr.copy(), k)

# Optimized version
rotated = rotate_right_optimized(arr.copy(), k)

print("Right rotated array:", rotated)
