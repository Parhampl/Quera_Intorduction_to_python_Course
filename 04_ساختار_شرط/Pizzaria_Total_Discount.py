# There is a pizzaria which randomly gives discount codes
# If there is s in inputs it gives 10% discount   s --> 10%
# If there is 7 in inputs it gives 5% discount   7 --> 5%
# If there is * in inputs it gives 30% discount   * --> 30%
# note: duplication of these characters in input doesnt affect on discount amount.
# However, if more than one of these characters appears they can be add to each other.
a, b, c = input().split()

Total_Discount = 0
if (a == "7" or b == "7" or c == "7"):
    Total_Discount += 5
if (a == "s" or b == "s" or c == "s"):
    Total_Discount += 10

if (a == "*" or b == "*" or c == "*"):
    Total_Discount += 30

print(Total_Discount)
