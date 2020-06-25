import concurrent.futures as futures
import math
import multiprocessing

from TestUtils import swap
from comparison.Insertion import insertionSort
def shellSort(array):
  end = len(array)
  if end <= 1:
    return
  gap = int(len(array) / 2)
  changed = True
  pool = futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
  while gap > 1 or changed:
    gap = int(gap / 2)
    changed = False
    threads = []
    for start in range(gap):
      if end / gap >= 128:
        threads.append(pool.submit(
            insertionSort,
            array,
            start,
            end,
            gap
        ))
        futures.wait(threads)
      else:
        insertionSort(array, start, end, gap)
