L=[]
for i in range(10):
    N=int(input())
    L.append(N%42)
print(len(set(L)))