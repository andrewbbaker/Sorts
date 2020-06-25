import math
from TestUtils import swap
def combSort(array): 
  gap = math.ceil((len(array) - 1) / 2)
  changed = False
  while gap > 1 or changed:
    changed = False
    for i in range(len(array) - gap):
      if array[i] > array[i + gap]:
        changed = True
        swap(array, i, i + gap)
    gap = max(1, min(math.ceil(gap / 2), gap - 1))
