class reverse_string:


    # 1st answer
    n="string"
    def reverse(n):
        l=list(n)
        print(l)
        l.reverse()
        return "".join(l)
    print(reverse(n))



    # 2nd answer
    n="string"
    print(n[::-1])
    