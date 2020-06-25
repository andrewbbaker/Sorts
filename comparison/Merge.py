import math
import multiprocessing
import threading

from comparison.Insertion import insertionSort

def merge(array, clone, start, middle, end):
  cloneIndex = start
  leftIndex = start
  rightIndex = middle
  while leftIndex < middle and rightIndex < end:
    if array[leftIndex] < array[rightIndex]:
      clone[cloneIndex] = array[leftIndex]
      leftIndex += 1
    else:
      clone[cloneIndex] = array[rightIndex]
      rightIndex += 1
    cloneIndex += 1
  for i in range(leftIndex, middle):
    clone[cloneIndex] = array[i]
    cloneIndex += 1
  for i in range(rightIndex, end):
    clone[cloneIndex] = array[i]
    cloneIndex += 1

  for i in range(start, end):
    array[i] = clone[i]

def mergeInPlaceSort(array, start=0, end=None):
  if end is None:
    end = len(array)
  middle = start + int((end - start) / 2)
  if (end - start <= 1):
    return
  mergeInPlaceSort(array, start, middle)
  mergeInPlaceSort(array, middle, end)
  while middle < end:
    if array[start] < array[middle]:
      start += 1
    else:
      a = array[middle]
      for i in range(middle, start, -1):
        array[i] = array[i - 1]
      array[start] = a
      start += 1
      middle += 1

def mergeSort(array, start=0, end=None, clone=None):
  if end is None:
    clone = array.copy()
    end = len(array)
  middle = start + int((end - start) / 2)
  if (end - start <= 1):
    return
  mergeSort(array, start, middle, clone)
  mergeSort(array, middle, end, clone)
  merge(array, clone, start, middle, end)

def mergeParallelSort(array, start=0, end=None, clone=None, splits=None):
  if end is None:
    clone = array.copy()
    end = len(array)
    splits = math.floor(math.log(multiprocessing.cpu_count(), 2)) + 1
  middle = start + int((end - start) / 2)
  if (end - start <= 1):
    return
  if splits > 0:
    m1 = threading.Thread(target=mergeParallelSort, args=(array, start, middle, clone, splits - 1))
    m2 = threading.Thread(target=mergeParallelSort, args=(array, middle, end, clone, splits - 1))
    m1.start()
    m2.start()
    m1.join()
    m2.join()
  else:
    mergeSort(array, start, middle, clone)
    mergeSort(array, middle, end, clone)
  merge(array, clone, start, middle, end)


def mergeInsertionSort(array, start=0, end=None, clone=None, insertion=32):
  if end is None:
    clone = array.copy()
    end = len(array)
  middle = start + int((end - start) / 2)
  if (end - start <= insertion):
    insertionSort(array, start, end)
    return
  mergeSort(array, start, middle, clone)
  mergeSort(array, middle, end, clone)
  merge(array, clone, start, middle, end)