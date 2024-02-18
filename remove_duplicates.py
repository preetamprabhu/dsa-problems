class remove_Duplicates:
    def removeDuplicates(arr,n):
        arr.sort()
        i=n-1
        # cant use for loop because u cant pop a element while iterating
        while i > 0:
            if (arr[i]==arr[i-1]):
                arr.pop(i)
            i-=1
        return len(arr)