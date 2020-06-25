from TestUtils import swap
def cocktailSort(array):
  start = 0
  end = len(array) - 1
  changed = True
  while changed:
    changed = False
    for i in range(start, end):
      if array[i] > array[i + 1]:
        swap(array, i, i + 1)
        changed = True
    end -= 1
    for i in range(end, start - 1, -1):
      if array[i] > array[i + 1]:
        swap(array, i, i + 1)
        changed = True
    start += 1
