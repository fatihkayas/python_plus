#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.


num = list(map(int, input("").split()))
if num[0] == num [1] or num[1] == num [2] or num[0] == num[2] :
  print("Toplam:", 0)
else :
  print(sum(num))
