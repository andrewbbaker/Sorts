from TestUtils import swap
def bubbleSort(array):
  for i in range(1, len(array)):
    sorted = True
    for j in range(len(array) - i):
      if array[j] > array[j + 1]:
        sorted = False
        swap(array, j, j + 1)
    if sorted:
      return