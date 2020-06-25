def pigeonHoleSort(array):
  if len(array) <= 1:
    return
  minVal = min(array)
  maxVal = max(array)
  pigeonHoles = [[] for i in range(maxVal - minVal + 1)]
  for item in array:
    pigeonHoles[item - minVal].append(item)
  i = 0
  for hole in pigeonHoles:
    for item in hole:
      array[i] = item
      i += 1