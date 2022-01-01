import time, random
def main():
	n = int(input("Введiть розмiр: "))
	arr = [random.randint(0,100000) for i in range(0,n)]
	Time = time.time()
	sort(arr)
	Time = time.time()-Time
	arr = sort(arr)
	print(f"Час в середньому: {Time}")
	Time = time.time()
	sort(arr)
	Time = time.time()-Time
	print(f"Час в найкращому: {Time}")
	Time = time.time()
	sort(arr[::-1])
	Time = time.time()-Time
	print(f"Час в найгiршому: {Time}")
def sort(num):
	for i in range(len(num)):
		if i+1 < len(num) and num[i] > num[i+1]:
			num[i],num[i+1]=num[i+1],num[i]
	largest = num[len(num)-1]
	C = [0] * (largest+1)
	for i in range(len(num)):
		C[num[i]] = C[num[i]] +1
	C[0] = C[0] - 1
	for i in range(1,largest+1):
		C[i] = C[i] + C[i-1]
	result = [None] * len(num)
	for j in reversed(num):
		result[C[j]] = j
		C[j] = C[j] - 1
	return result
if __name__ == "__main__":
	main()
	input("Press F to respect")
