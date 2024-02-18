class left_rotation:
    def rotateArray(arr: list, k: int) -> list:
        n=len(arr)
        temp=arr[0:k]
        for i in range(k,n):
            arr[i-k]=arr[i]
        arr[n-k:]=temp
        return arr