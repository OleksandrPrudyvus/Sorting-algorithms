import random
import time
def main():
    arr = []
    num = int(input("Pleass enter number: "))
    for i in range(num):
        arr.append(random.randint(0,10000000))

    Time = time.time()
    heap_sort(arr)  
    Time = time.time()-Time
    print(f"Час середнього випадку: {Time}")
    Time = time.time()
    heap_sort(arr)  
    Time = time.time()-Time
    print(f"Час найкращого випадку: {Time}")
    arr = arr[::-1]
    Time = time.time()
    heap_sort(arr)  
    Time = time.time()-Time
    print(f"Час найгіршого випадку: {Time}")
def Heapify(nums, heaps, root):  
    # Використовуємо формулу про гілля бінарного дерева
    large = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    # якщо лівий потомок є і він більший за цей найбільший, міняєм їх
    if left < heaps and nums[left] > nums[large]:
        large = left
    # теж для правого 
    if right < heaps and nums[right] > nums[large]:
        large = right
    # якщо найбільший вже не корінь то міняєм місцями
    if large != root:
        nums[root], nums[large] = nums[large], nums[root]
        # викликаємо знов щоб удостовіритись що наш елемент найбільший
        Heapify(nums, heaps, large)
def heap_sort(nums):  
    n = len(nums)
    # створюємо кучу зі списку
    for i in range(n, -1, -1):
        Heapify(nums, n, i)
    # переміщуємо корінь в кінець
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        Heapify(nums, i, 0)
if __name__ == "__main__":
    main()