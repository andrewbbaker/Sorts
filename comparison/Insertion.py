from TestUtils import swap
def insertionSort(array, start=0, end=None, gap=1):
  if not end:
    end = len(array)
  for i in range(start + gap, end):
    j = i
    while j >= start + gap and array[j] < array[j - gap]:
      swap(array, j, j-gap)
      j -= gap
