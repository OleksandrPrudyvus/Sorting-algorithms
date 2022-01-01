from random import randint
import time
def main():
    arr = []
    r = int(input("Pleas enter number: "))
    for i in range(r):
        arr.append(randint(0, 10000000))
    #print(arr,"\n")
    Time = time.time()
    sorts(arr)
    Time = time.time() - Time
    print(f"Перший час {Time}")
    arr = sorts(arr)
    Time=time.time()
    sorts(arr)
    Time = time.time() - Time
    print(f"Найкращий випадок: {Time}")
    Time = time.time()
    sorts(arr[::-1])
    print(f"Найгірший випадок: {time.time()-Time}")
def sorts(arr):
	if len(arr) == 1:
		return arr
	middle = len(arr)//2
	left = sorts(arr[:middle])
	right = sorts(arr[middle:])
	return splits(left, right)
#функція для об'єднання масиву:)
def splits(l, r):
	temp = []
	i = j = 0
	while i< len(l) and j <len(r):
		if l[i]<r[j]:
			temp.append(l[i])
			i+=1
		else:
			temp.append(r[j])
			j+=1
	if i < len(l):
		temp += l[i:]
	if j < len(r):
		temp += r[j:]
	return temp
if __name__ == "__main__":
    main()
    x = input("Press enter for exit")
