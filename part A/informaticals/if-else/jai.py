x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())
if((x==x2 and y == y2)):
    print("NO")
elif(x==x2 and y!=y2 ):
    print("YES")
elif(x!=x2 and y==y2):
    print("YES")
elif(x,x2,y,y2 > 8 or x,x2,y,y2<1):
    print("NO")