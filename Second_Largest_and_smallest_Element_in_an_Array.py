class brute_force:
    def getSecondOrderElements1(n: int,  a: [int]) -> [int]:
        if n==1:
            return a[0]
        a.sort()
        return a[-2]," ",a[1]
        
class optimal:
    def getSecondOrderElements2(n: int,  a: [int]) -> [int]:
    # Initializing the driver variables.
        small = int(1e9)
        secondSmall = int(1e9)
        large = int(-1e9)
        secondLarge = int(-1e9)

        # Iterating over an array and calculating the smaller and larger numbers.
        for i in range(n):
            small = min(small, a[i])
            large = max(large, a[i])

        # Iterating again and updating the second order numbers.
        for i in range(n):
            if (a[i] < secondSmall and a[i] != small):
                secondSmall = a[i]
            if (a[i] > secondLarge and a[i] != large):
                secondLarge = a[i]

        return [secondLarge, secondSmall]       