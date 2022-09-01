# Code related to Question 9
LB_Weight= [150, 155, 145, 148]
Kg_Weight=[]
for i in LB_Weight:
    Kg_Weight.append( round(float(0.45359237* i), 2))
print("Weights in Killo-gram ", Kg_Weight)