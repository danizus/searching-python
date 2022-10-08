from turtle import pos


pos=-1
def search(list,n):
    low=0
    up=len(list)-1
    for i in range(len(list)):
        mid=(low+up)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                low=mid+1
            elif list[mid]>n:
                up=mid-1
    return False



list=[1,2,3,4,5,6,]
n=int(input('enter number'))
if search(list,n):
    print("found at",pos)
else:
    print('not found')

input()