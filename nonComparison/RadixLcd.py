import math
bucketSize = 8
def radixLsdSort(array):
  if len(array) <= 1:
    return
  maxVal = max(array)
  buckets = [[] for i in range(bucketSize)]
  for level in range(math.ceil(math.log(maxVal, bucketSize))):
    for item in array:
      buckets[int((item / (bucketSize ** level)) % bucketSize)].append(item)  
    i = 0
    for bucket in buckets:
      for item in bucket:
        array[i] = item
        i += 1
      bucket.clear()
