import concurrent.futures as futures
import math
import multiprocessing

from TestUtils import swap
from comparison.Insertion import insertionSort

def mergeUp(array, start, end):
  if end - start <= 1:
    return
  gap = int(2 ** (math.ceil(math.log(end - start, 2)) - 1))
  middle = start + gap
  missingNumbers = (gap * 2) - (end - start)
  if missingNumbers > 0:
    if array[start] > array[middle - 1]:
      for left in range(start, start + gap - missingNumbers):
        right = left + gap
        if array[left] > array[right]:
          swap(array, left, right)
    else:
      for left in range(start + missingNumbers, middle):
        right = left + gap - missingNumbers
        if array[left] > array[right]:
          swap(array, left, right)
    mergeUp(array, start, middle)
    mergeUp(array, middle, end)
  else:
    for left in range(start, middle):
      right = left + gap
      if right < end:
        if array[left] > array[right]:
          swap(array, left, right)
    mergeUp(array, start, middle)
    mergeUp(array, middle, end)

def mergeDown(array, start, end, falseBottom = None):
  if end - start <= 1:
    return
  if falseBottom and falseBottom >= end:
    return
  gap = int(2 ** (math.ceil(math.log(end - start, 2)) - 1))
  if falseBottom and end - (gap * 2) > falseBottom:
    falseBottom = None
  missingNumbers = (gap * 2) - (end - start)
  end = min(len(array), end)
  middle = start + gap
  if missingNumbers > 0 and falseBottom == None:
    holding = [array[index] for index in range(start, start + missingNumbers)]
    for i in range(gap - missingNumbers):
      left = middle - gap + missingNumbers + i
      right = middle + i
      minVal = min(array[left], array[right])
      maxVal = max(array[left], array[right])
      array[start + i] = maxVal
      array[middle + i] = minVal
    middle = start + gap - missingNumbers
    for i in range(missingNumbers):
      array[middle + i] = holding[i]
    mergeDown(array, middle - gap, middle, falseBottom=start)
    mergeDown(array, middle, end)
  else:
    for left in range(start, middle):
      if not falseBottom or left >= falseBottom:
        right = left + gap
        if array[left] < array[right]:
          swap(array, left, right)
    mergeDown(array, start, middle, falseBottom=falseBottom)
    mergeDown(array, middle, end, falseBottom=falseBottom)

def bitonicSort(array):
  end = len(array)
  if end <= 1:
    return
  sortSize = 2
  while sortSize <= end:
    for i in range(0, end, sortSize * 2):
      middle = i + sortSize
      mergeUp(array, i, min(middle, end))
      mergeDown(array, middle, min(end, i + (sortSize * 2)))
    sortSize *= 2
  mergeUp(array, 0, end)

