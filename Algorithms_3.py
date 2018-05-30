# copy from one array to another

print("Enter the number of elements in array")
N = int(input())
A = [0] * N
B = [0] * N

print("Fill up array A")
for k in range(N):
    print("Element №", k+1)
    A[k] = int(input())

for k in range(N):
    B[k] = A[k]


print("Array A -", A)
print( "Array B -", B)
