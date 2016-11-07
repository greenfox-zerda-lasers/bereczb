from prettytable import from_csv

fp = open("lottery/topfive.csv", "r")
pt = from_csv(fp)
fp.close()

print(pt)
