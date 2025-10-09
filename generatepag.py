def f(arr,k):
    for i in range(0,len(arr),k):
        return arr[i:i+k]

f([1,2,3,4,5,6],2)