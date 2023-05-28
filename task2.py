N = int(input())
A = [i for i in range(N)]
X = int(input())
b = [abs(A[i]-X) for i in range(len(A))]
print(A[b.index(min(b))])