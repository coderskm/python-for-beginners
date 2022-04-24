def sum(l,*elements):
  sum = 0
  for x in elements:
    sum=sum+x
  return sum,l

print(sum(3,2,3,4))