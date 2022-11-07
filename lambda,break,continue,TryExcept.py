def myfunc(n):
  return lambda a : a * n

aaa = myfunc(2)


print(aaa(5))
#prints 5*2

b = lambda a: a%2 == 0

print(b(6))

j = 0

for i in range(6):
    j = j + 2
    print("i = ",i,"j = ",j)
    if j == 10:
        break

for i in range(9):
  if i == 3:
    continue
  print(i)

try:
  hello
except:
  print(1)
