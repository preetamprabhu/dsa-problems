class recursionfibonnaci:
    import math

    def f(n):
        if(n<0):
            return("invalid")
        if(n==1 or n==0):
            return n
        return f(n-1)+f(n-2)               #this code is O(2^n) exponential time complexity
    # n=int(input())
    print(f(4))


    # import math 
    # print('pi is', math. pi) 
    # print('cos(pi) is', math. cos(math. pi))