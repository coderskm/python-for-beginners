a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

def operations(x,y):
  s = x+y
  p = x*y
  return s,p

sum,prod = operations(a,b)
a = str(a)
b = str(b)
print(f"{a}+{b}={sum}")
print(f"{a}X{b}={prod}")