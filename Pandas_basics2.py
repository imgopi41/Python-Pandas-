import pandas as pd

#Creating DataFrame using List

a = ["AAA","BBB","CCC"]
b = pd.DataFrame(a)
# print(b)

#Creating DataFrame using list of list

c = [["AAA","BBB","CCC"],["DDD","EEE","FFF"]]
d = pd.DataFrame(c)
# print(d)

#Creating DataFrame using Dictonary

E = {"Name":["AAA","BBB","CCC"],"Var":["EEE","FFF","GGG"]}
F = pd.DataFrame(E)
# print(F)

#Creating DataFrame list in Dictonary

G = [{"Names":"AAA","Student":"BBB","Var":"CCC"},{"Names":"10","Student":"20","Var":"30"}]
H = pd.DataFrame(G)
# print(H)

#Creating DataFrame by using Zip

I = [10,20,30]
J = ["AAA","BBB","CCC"]
L = pd.DataFrame(zip(I,J))
print(L)


