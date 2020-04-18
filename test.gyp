l1=input()
l2=input()

max_len=len(l1) if len(l1)>len(l2) else len(l2)
l1=l1.zfill(max_len)
l2=l2.zfill(max_len)

a1=list(l1)
a2=list(l2)
a3=[0 for _ in range(max_len+1)]

for i in range(max_len-1,-1,-1):
    index_sum=a3[i+1]+int(a2[i])+int(a1[i])
    less=index_sum-10
    a3[i+1]=index_sum%10
    a3[i]=1 if less>0 else 0
if a3[0]==0:
    a3.pop(0)
a33=[str(i) for i in a3]
print(''.join(a33))