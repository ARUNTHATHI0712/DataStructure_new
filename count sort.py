def Count_sort(li):
    max1=max(li)
    cli=[0]*(max1+1)
    print(cli)
    for i in li:
        cli[i]+=1
    j=0
    print(cli)
    for i in range(len(cli)):
        while(cli[i]>0):
            li[j]=i
            cli[i]-=1
            print(cli)
            j+=1
    print(li)
Count_sort([2,4,5,6,7,4,5,6,7,8,4,5,6,7,9])
