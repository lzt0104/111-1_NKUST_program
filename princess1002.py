n11 = eval(input(""))
n12 = eval(input(""))

n21 = eval(input(""))
n22 = eval(input(""))


print("|{0:07d} {1:>+10,.2f}|".format(n11,n12))
print("|{0:07d} {1:>+10,.2f}|".format(n21,n22))
print("|{0:^7s} {1:>10,.2%}|".format("ratio", n12 / n22))