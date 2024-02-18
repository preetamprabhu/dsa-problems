class brute_force:
    def getSecondOrderElements(n: int,  a: [int]) -> [int]:
        if n==1:
            return a[0]
        a.sort()
        return a[-2]," ",a[1]
        