from TestUtils import swap
def heapSort(array):
  for i in range(1, len(array)):
    heapUp(array, i)
  for i in range(len(array) - 1, 0, -1):
    swap(array, 0, i)
    heapDown(array, 0, i)

def heapUp(array, position):
  parent = int((position - 1) / 2)
  if array[position] > array[parent]:
    swap(array, position, parent)
    heapUp(array, parent)

def heapDown(array, position, length):
  child = (position + 1) * 2 - 1
  if child >= length:
    return
  if child + 1 < length:
    if (array[child] < array[child + 1]):
      child += 1
  if array[position] < array[child]:
    swap(array, position, child)
    heapDown(array, child, length)
    return
