n=int(input('enter a num:'))
a=[]
for i in range (n):
    a.append(int(input('enter a list item:')))
search_item=int(input('enter a search item:'))
found=False
for i in range(len(a)):
    
    if (a[i]==search_item):
        found=True
        break
if found:
        print(search_item,'element are found in list at position',i)
else:
        print("search element is not found")
