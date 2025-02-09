arr = [0]*10
for i in range(5):
    arr[i] = i
print(arr)
# 数组arr中前五位有数据
# 我想在第n位插入数据,n小于等于5
n = eval(input(':'))
for j in range(5,n,-1):
    arr[j] = arr[j-1]
arr[n] = 666
print(arr)