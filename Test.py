import functools
import math
import random
import sys
import TestUtils
import time

from pprint import pprint as pp

import TestUtils

from comparison.Bitonic import bitonicSort
from comparison.Bubble import bubbleSort
from comparison.Cocktail import cocktailSort
from comparison.Comb import combSort
from comparison.Gnome import gnomeSort
from comparison.Heap import heapSort
from comparison.Insertion import insertionSort
from comparison.Merge import mergeInPlaceSort, mergeInsertionSort, mergeParallelSort, mergeSort
from comparison.Quick import quickSort
from comparison.Selection import selectionSort
from comparison.Shell import shellSort
from comparison.Stooge import stoogeSort
from comparison.Tim import timSort
from nonComparison.PigeonHole import pigeonHoleSort
from nonComparison.RadixGcd import radixGcdSort, radixGcdParallelSort
from nonComparison.RadixLcd import radixLsdSort

sorts = [bitonicSort, heapSort, mergeInsertionSort, mergeParallelSort, mergeSort, pigeonHoleSort, quickSort, radixGcdParallelSort, radixGcdSort, radixLsdSort, shellSort, timSort]
badSorts = [bubbleSort, cocktailSort, combSort, gnomeSort, insertionSort, mergeInPlaceSort, selectionSort, shellSort]
resultFunctions = [TestUtils.average, TestUtils.total]
sizes = [0, 1, 5]
[sizes.append(10**i) for i in range(1, 5)]
arrays = {}
testResults = {}
printOutput = True

def createArraysOfSize(size, count):
  arrays[size] = []
  for i in range(count):
    random.seed(i)
    array = list(range(size))
    random.shuffle(array)
    arrays[size].append(array)

def arraySizes():
  arrayCount = max(sizes)
  if arrayCount <= 8:
    arrayCount = 10
  else:
    arrayCount = math.ceil(math.log(arrayCount, 2) ** 2)
  return [arrayCount for i in range(len(sizes))]

def createArrays():
  for size, count in zip(sizes, arraySizes()):
    print("\tCreating {} arrays of size {}".format(count, size))
    testResults[size] = {}
    createArraysOfSize(size, count)

def assertArraySorted(array, size):
  assert len(array) == size, "Array is of length {} and should be {}: {}".format(len(array), size, array)
  if (len(array) == 0):
    return
  for i in range(0, len(array)):
    assert array[i] == i, "array[{}] = {}: {}".format(i, array[i], array)

def runTest(sort, array):
  copy = array.copy()
  length = len(array)
  start = time.time()
  sort(copy)
  end = time.time()
  assertArraySorted(copy, length)
  testResults[len(array)][sort.__name__].append(end - start)

def runSort(sort):
  for size in sizes:
    print("\trunning {:20} of size {:<6}\t".format(sort.__name__, size), end="")
    testResults[size][sort.__name__] = []
    lineLength = 10**2
    if len(arrays[size]) > lineLength:
      print()
    for i in range(len(arrays[size])):
      if printOutput:
        sys.stdout.write(str(i % 10))
        sys.stdout.flush()
        lineBreak = lineLength
        lineBroken = False
        while lineBreak < len(arrays[size]):
          if i % lineBreak == lineBreak - 1:
            print()
            lineBroken = True
          lineBreak *= 10
        if not lineBroken and i % 10 == 9:
          print(" ", end= "")
      runTest(sort, arrays[size][i])
    print()

def processResults():
  for function in resultFunctions:
    function(testResults, sorts, sizes)

def runAllTests(useBadSorts=False, badSortExpections=[]):
  createArrays()
  if useBadSorts:
    for sort in badSorts:
      if sort not in badSortExpections:
        sorts.append(sort)
  for sort in sorts:
    runSort(sort)
  processResults()

def runSingleTest(sort):
  print(sort.__name__)
  sorts.clear()
  sorts.append(sort)
  runAllTests()

def createdSortedArray(size, count):
  arrays[size] = [list(range(size))]

def createReverseArray(size, count):
  array = list(range(size))
  array.reverse()
  arrays[size] = [array]

def createOneWrongArray(size, count):
  arrays[size] = []
  for i in range(count):
    random.seed(i)
    array = list(range(size))
    if size > 1:
      a = b = -1
      while a == b:
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
      TestUtils.swap(array, a, b)
    arrays[size].append(array)

def oneOffArray(size, count):
  array = list(range(size))
  for i in range(1, size):
    TestUtils.swap(array, i - 1, i)
    

# runSingleTest(quickSort)
runAllTests()

# specialArrays = [createdSortedArray, createReverseArray, createOneWrongArray]
# for arrayFunc in specialArrays:
#   print(arrayFunc.__name__)
#   createArraysOfSize = arrayFunc
#   runAllTests()

