from math import floor, log
import threading
import multiprocessing
bucketSize = 8
def radixGcdSort(array, level=None, bucketSize=bucketSize):
  if len(array) <= 1:
    return
  if level is None:
    level = floor(log(max(array), bucketSize))
  buckets = [[] for i in range(bucketSize)]
  for item in array:
    # print("{} {} {}".format(item, bucketSize, level))
    buckets[int((item / (bucketSize ** level)) % bucketSize)].append(item)
  for bucket in buckets:
    radixGcdSort(bucket, level - 1, bucketSize)
  i = 0
  for bucket in buckets:
    for item in bucket:
      array[i] = item
      i += 1
    bucket.clear()

def radixGcdParallelSort(array):
  if len(array) <= 1:
    return
  buckets = [[] for i in range(multiprocessing.cpu_count())]
  level = floor(log(max(array), len(buckets)))
  for item in array:
      buckets[int((item / (len(buckets) ** level)) % len(buckets))].append(item)
  threads = []
  for bucket in buckets:
    threads.append(threading.Thread(target=radixGcdSort, args=(bucket, level - 1, len(buckets))))
    threads[-1].start()
  for thread in threads:
    thread.join()
  i = 0
  for bucket in buckets:
    for item in bucket:
      array[i] = item
      i += 1
    bucket.clear()
