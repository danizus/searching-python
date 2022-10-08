from operator import truediv
position=0

def search(list,n):
    lenght=len(list)
    for i in range(lenght):
        if list[i]==n:
            globals() ['position']=i
            return True
    return False

    

list=[1,3,4,5,7,8,0]
n=int(input('enter number : '))
if search(list,n):
    print("found at",position)
else:
    print('not found')
input()

    