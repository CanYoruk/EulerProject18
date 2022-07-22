#
import time
t0 = time.time()
row1 = [75]
row2 = [95,64]
row3 = [17,47,82]
row4 = [18,35,87,10]
row5 = [20,4,82,47,65]
row6 = [19,1,23,75,3,34]
row7 = [88,2,77,73,7,63,67]
row8 = [99,65,4,28,6,16,70,92]
row9 = [41,41,26,56,83,40,80,70,33]
row10 = [41,48,72,33,47,32,37,16,94,29]
row11 = [53,71,44,65,25,43,91,52,97,51,14]
row12 = [70,11,33,28,77,73,17,78,39,68,17,57]
row13 = [91,71,52,38,17,14,91,43,58,50,27,29,48]
row14 = [63,66,4,68,89,53,67,30,73,16,69,87,40,31]
row15 = [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

def nextrow(top,bottom):
  newrow = []
  for x in range(len(top)):
    newrow.append("")#creating a list with the required number of items
  for i in range(len(newrow)):
    winner = 0
    if bottom[i] < bottom[i+1]:
      winner = bottom[i+1]
    else:
      winner = bottom[i]
    newrow[i] = top[i] + winner
  return newrow
    

#
row14 = nextrow(row14,row15)
row13 = nextrow(row13,row14)
row12 = nextrow(row12,row13)
row11 = nextrow(row11,row12)
row10 = nextrow(row10,row11)
row9 = nextrow(row9,row10)
row8 = nextrow(row8,row9)
row7 = nextrow(row7,row8)
row6 = nextrow(row6,row7)
row5 = nextrow(row5,row6)
row4 = nextrow(row4,row5)
row3 = nextrow(row3,row4)
row2 = nextrow(row2,row3)
row1 = nextrow(row1,row2)
print(row1)
t1 = time.time()
print(t1-t0)
#answer = 1074 (correct)
#0.0050048828125 seconds
