def Ackermann(m,n):
    if not isinstance(m, int) or not isinstance(n, int):
        return None
    else:
        if m<0 or n<0:
            return None
        else:
            if m == 0:
                return n+1
            elif m>0 and n==0:
                return Ackermann(m-1, 1)
            elif m>0 and n>0:
                return Ackermann(m-1,Ackermann(m, n-1))

print(Ackermann(1,1))