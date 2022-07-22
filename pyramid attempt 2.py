#dictionary approach
#brute force
import time
t0 = time.time()
pyramid = {
  67 : [70,92],
  63 : [16,70],
  7 : [6,16],
  73 : [28,6],
  77 : [4,28],
  2 : [65,4],
  88 : [99,65],
  75 : [73,7],
  75 : [95,64],
  95 : [17,47],
  64 : [47,82],
  17 : [18,35],
  47 : [35,87],
  82 : [87,10],
  18 : [20,4],
  35 : [4,82],
  87 : [82,47],
  10 : [47,65],
  20 : [19,1],
  4 : [1,23],
  82 : [23,75],
  47 : [75,3],
  65 : [3,34],
  19 : [88,2],
  1 : [2,77],
  23 : [77,73],
  3 : [7,63],
  34 : [63,67]
  }
sums = []
for i in range(2):
  p2nd = pyramid[75][i]
  total = 75 + p2nd
  for j in range(2):
    p3rd = pyramid[p2nd][j]
    total = total + p3rd
    for k in range(2):
      p4th = pyramid[p3rd][k]
      total = total + p4th
      for l in range(2):
        p5th = pyramid[p4th][l]
        total = total + p5th
        sums.append(total)
        total = total - p5th
      total = total - p4th
    total = total - p3rd
sums.sort(reverse = True)
print(sums[0])
t1 = time.time()
print(t1-t0)
#works until the 5th row
#takes 0.012 seconds

  
  
