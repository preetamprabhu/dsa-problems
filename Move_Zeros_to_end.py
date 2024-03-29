class Move_Zeros_to_end:
    def moveZeros(n: int,  a: [int]) -> [int]:
        j = -1
        # Place the pointer j
        for i in range(n):
            if a[i] == 0:
                j = i        #here j is the first encountered 0 in the array
                break
        
        # No non-zero elements
        if j == -1:
            return a
        
        # Move the pointers i and j and swap accordingly
        for i in range(j + 1, n):
            if a[i] != 0:
                a[i], a[j] = a[j], a[i]
                j += 1
        
        return a # array