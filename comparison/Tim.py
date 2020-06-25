import concurrent.futures as futures
import math
import multiprocessing

import comparison.Insertion as Insertion
import comparison.Merge as Merge

insertionCount = 32
def timSort(array):
  pool = futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
  arrayLen = len(array)
  if arrayLen <= insertionCount:
    Insertion.insertionSort(array, 0, arrayLen)
    return
  runs = math.ceil(arrayLen / insertionCount)
  threads = []
  for i in range(runs):
    fut = pool.submit(
        Insertion.insertionSort, 
        array,
        i * insertionCount,
        min((i + 1) * (insertionCount), arrayLen)
    )
    threads.append(fut)
  futures.wait(threads)
  gap = insertionCount
  clone = array.copy()
  while gap < arrayLen:
    gap *= 2
    threads.clear()
    [threads.append(pool.submit(Merge.merge,
                                array,
                                clone,
                                i * gap,
                                int(min((i * gap) + (gap / 2), arrayLen)),
                                int(min((i + 1) * gap, arrayLen))
                )) for i in range(math.ceil(arrayLen / (gap)))]
    futures.wait(threads)
