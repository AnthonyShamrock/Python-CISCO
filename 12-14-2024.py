john,mary,adam = 1,2,3
total_apples = 0

for index,value in dict(locals()).items():
  if "__" in index or "total_apples" == index:
    continue
  print(index,value)
  total_apples += int(value)

print('Total number of apples: {}'.format(str(total_apples)))
