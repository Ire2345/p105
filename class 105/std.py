import csv
import math

with open("data22.csv", newline="") as f:
  reader=csv.reader(f)
  file_data=list(reader)

data=file_data[0]

def mean(data):
  n=len(data)-1
  sum=0
  for x in data:
    sum+=int(x)
  mean=sum/n

  return mean

squaredlist=[]
for d in data:
  s=int(d)-mean(data)
  s=s**2
  squaredlist.append(s)

sum=0

for c in squaredlist:
  sum=sum+c

result=sum/(len(data)-1)
standarddeviation=math.sqrt(result)
print(standarddeviation)