def mergesort(list1):

    ret = []
    if (len(list1)==1):
        return 1
    half = len(list1)//2
    lower = mergesort(list1[:half])
    upper = mergesort(list1[half:])
    lenlow  = len(lower)
    lenupp = len(upper)
    i,j = 0,0
    while(i!=lenlow or j!=lenupp):
        if(i!=lenlow and (j==lenupp or lower[i]<upper[j])):
            ret.append(lower[i])
            i+=1
        else:
            ret.append(upper[j])
            j+=1
    return ret

lis = [4,2,3,8,8,3,6,1,0]

print(mergesort(lis))