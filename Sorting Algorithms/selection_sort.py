def selection(arr,i):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    for i in range(0,n):
        print(arr[i])
selection([23, 87, 4, 56, 12, 99, 31, 65, 8, 42],1)