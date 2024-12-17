def selectionSort(list1):
    for i in range(len(list1)):
        mini = i
        # print(mini)
        for j in range(i+1,len(list1)):
            if list1[j]<list1[mini]:
                mini=j
        list1[i],list1[mini]=list1[mini],list1[i]
        print(list1)
lis = [4,2,3,8,8,3,6,1,0]
print(lis)
selectionSort(lis)