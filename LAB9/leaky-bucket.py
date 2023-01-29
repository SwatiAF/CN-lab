capacity = int(input("enter the buckey size: \n")
outrate = int(input("enter the outflow rate: \n")
buffer = 0
n = 0
              
while n < 5:
  inflow = int(input("enter momentary inflow: ")
  buffer += inflow
  if buffer >= capacity:
    print("bucket full")
    break
  buffer = outrate
  if buffer < 0:
    buffer = 0
  print(buffer)
  n += 1

