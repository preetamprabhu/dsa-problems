class left_rotate_index_by_one:
    def rotateArray(arr: [int], n: int) -> [int]:
    # Write your code from here.
        temp=arr[0]
        for i in range(1,n):
            arr[i-1]=arr[i]
        arr[n-1]=temp
        return arr
    