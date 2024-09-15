def binary_search(start,end,a,k):
 for i in a:
        mid=(start+end)//2
        if a[mid]==k:
            print(mid)
            break
        elif a[mid]>k:
            return binary_search(start,mid,a,k)
            break
        else:
            return binary_search(mid+1,end,a,k)
n=int(input('enter a number of element:'))
a=[]
for i in range(n):
    a.append(int(input('enter a items:')))
for i in range(0,n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print('the sorted list is :',a)

k=int(input('enter a search item:'))

print(binary_search(0,n-1,a,k))
