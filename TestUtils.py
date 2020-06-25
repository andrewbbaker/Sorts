import math
import statistics

def swap(array, index1, index2):
  # print("swap")
  if index1 != index2:
    # print("\t{}={} <-> {}={}".format(index1, array[index1], index2, array[index2]))
    a = array[index1]
    array[index1] = array[index2]
    array[index2] = a
  # print("{} <-> {}".format(array[index1], array[index2]))

def average(testResults, sorts, sizes):
  for size in sizes:
    print("\tAverage of size {}:".format(size))
    for sort in sorts:
      print("\t\t{:{width}}: {}".format(sort.__name__, statistics.mean(testResults[size][sort.__name__]), width=20))

def standardDeviation(testResults, sorts, sizes):
  for size in sizes:
    print("\tStandard Deviation of size {}:".format(size))
    for sort in sorts:
      if (len(testResults[size][sort.__name__]) > 1):
        print("\t\t{:{width}}: {}".format(sort.__name__, statistics.stdev(testResults[size][sort.__name__]), width=20))

def total(testResults, sorts, sizes):
  print("\tTotal time:")
  for sort in sorts:
    total = 0
    for size in sizes:
      total += sum(testResults[size][sort.__name__])
    print("\t\t{:{width}}: {}".format(sort.__name__, total, width=20))
