file = open("sales analyzer,txt.txt", "r")

sales = []

for line in file:
    sales.append(float(line.strip()))

file.close()

total_sales = sum(sales)
cost_price = float(input("total cost price:"))

profit = total_sales - cost_price

print("\ntotal sales:", total_sales)
 
if profit > 100000:
    print("profit :", profit)
    print("criteria: , excellent")
elif profit < 0:
    print("profit :", profit)
    print("criteria: , good ")
elif profit == 0:
    print("profit :" , profit)
    print("criteria: , average")
else:
 print("loss:" , abs(profit))
 print("criteria: , worst")



