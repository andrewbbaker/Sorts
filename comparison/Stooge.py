from TestUtils import swap
from math import ceil
def stoogeSort(array, start=0, end=None):
  if end == None:
    end = len(array)
  if array[start] > array[end - 1]:
    swap(array, start, end - 1)
  if start + 2 >= end:
    return
  increment = ceil((2/3) * (end - start))
  stoogeSort(array, start, start + increment)
  stoogeSort(array, end - increment, end)
  stoogeSort(array, start, start + increment)
  