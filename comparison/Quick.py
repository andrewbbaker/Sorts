from TestUtils import swap
import random
def quickSort(array, start=0, end=None):
  if not end:
    end = len(array)
  if end - start <= 1:
    return
  
  swap(array, start, random.randint(start, end - 1))
  leftIndex = start + 1
  rightIndex = end - 1
  while leftIndex < rightIndex:
    while leftIndex < rightIndex and array[rightIndex] > array[start]:
      rightIndex -= 1
    while leftIndex < rightIndex and array[leftIndex] < array[start]:
      leftIndex += 1
    if leftIndex != rightIndex:
      swap(array, leftIndex, rightIndex)
  if array[start] > array[rightIndex]:
    swap(array, start, rightIndex)
  else:
    start += 1
  quickSort(array, start=start, end=rightIndex)
  quickSort(array, start=rightIndex, end=end)
