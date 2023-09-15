n=int(input())
S=list(map(int,input().split()))
sum=0
d=0
while d<n-1:
    sum+=S[d]
    d+=1
summa=n*(n+1)/2
print(int(summa-sum))