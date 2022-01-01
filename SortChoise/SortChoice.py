import random
import time
def main():
    i = int(input("Введи кількість об'єктів в  масиві "))
    array = []
    for n in range(i):
        array.append(random.randint(0, 100000))
    print(array)
    print()
    #First ,random numbers array
    printFirst(array)
    print()
    printSecond(array)
    print()
    array2 = array[::-1]
    print()
    printThird(array2)
def sort(array):
    for i in range(len(array)):
    	mina = i
    	for j in range(i,len(array)):
    		if array[mina]>array[j]:
    			mina = j
    	array[i],array[mina]= array[mina],array[i]
    return array
def sort2(array2):
	for i in range(len(array2)):
		mina1 = i
		for j in range(i,len(array2)):
			if array2[mina1]>array2[j]:
				mina1 = j
				array2[i],array2[mina1]= array2[mina1],array2[i]
	return array2
def printFirst(array):
    FirstStartTime = time.time()
    sort(array)
    timeFirst = time.time()-FirstStartTime
    #print(array)
    print("Час з найпершими, рандомними числами :",timeFirst)
    return array
def printSecond(array):
    SecondStartTime = time.time()
    sort(array)
    timeSecond = time.time()-SecondStartTime
    #print(array)
    print("Час найкращого випадку:" ,timeSecond)
def printThird(array2):
    ThirdStartTime = time.time()
    sort2(array2)
    timeThird = time.time()-ThirdStartTime
    #print(array2)
    print("Час найгіршого випадку:",timeThird)
if __name__ == "__main__":
    main()
