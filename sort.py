##桶排序时间复杂度最低o(M+N),冒泡排序时间复杂度是o(N**2),快速排序平均时间复杂度为o(N*logN)
input=[6,1,2,7,9,3,4,5,10,8]

##桶排序
res=[0 for _ in range(11)]
for i in range(len(input)):
	res[input[i]]+=1

for i in range(11):
	for j in range(res[i]):
		print(i)

#冒泡排序
n=len(input)
for i in range(n-1):		##n个数排序，总共需要进行n-1趟
	for j in range(n-i-1):	##由于每一趟可以排好一个数，因而我们不需要管已经排好的数
		if input[j+1]>input[j]:
			t=input[j]
			input[j]=input[j+1]
			input[j+1]=t
print(input)

##快速排序
def quicksort(arr,left,right):
	if left>right:
		return
	temp=arr[left]		##temp中存放的就是基准数
	i,j=left,right
	while i!=j:
		while arr[j]>=temp and i<j:		##顺序很重要，要先从右往左找
			j-=1
		while arr[i]<=temp and i<j:		##再从左往右找
			i+=1	
		if i<j:							##交换两个数在数组中的位置，当i和j没有相遇时	
			t=arr[i]
			arr[i]=arr[j]
			arr[j]=t
	arr[left]=arr[i]			##最终将基准数归位
	arr[i]=temp
	quicksort(arr,left,i-1)		##继续处理左边的，这是一个递归的过程
	quicksort(arr,i+1,right)	##继续处理右边的，这是一个递归的过程
	return

def main():
	n=len(input)
	quicksort(input,0,n-1)
	print(input)

if __name__ == '__main__':
	main()


##第一章题解(题目说明:n<=100,1<=isbn<=1000)
stu_num=10
isbn=[20,40,32,67,40,20,89,300,400,15]

##先去重后排序，桶排序
res=[0 for i in range(1001)]
for item in isbn:
	res[item]=1
for i in range(len(res)):
	if res[i]!=0:
		print(i)

##先排序后去重，冒泡排序或者快速排序
quicksort(isbn,0,stu_num-1)
for i in range(1,stu_num):
	if isbn[i]!=isbn[i-1]:
		print(isbn[i])



