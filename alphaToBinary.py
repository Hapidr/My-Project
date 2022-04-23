import math

from pyparsing import Word


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

word = input("Masukkan kata: ")

for i in toBinary(word):
  print(i, end=' ')