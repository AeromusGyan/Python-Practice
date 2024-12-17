def TOH(n,src,dest,aux):
    if n==1:
        print("move disk 1 from",src,"to destinaation",dest)
        return
    TOH(n-1,src,aux,dest)
    print("move disk",n,"from",src,"to destinaation",dest)
    TOH(n-1,aux,dest,src)
n = 4
print(TOH(n,'A','B','C'))
    