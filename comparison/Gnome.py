from TestUtils import swap
def gnomeSort(array):
  index = 1
  while index < len(array):
    if index == 0:
      index = 1
    if array[index - 1] > array[index]:
      swap(array, index - 1, index)
      index -= 1
    else:
      index += 1