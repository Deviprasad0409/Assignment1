# Code related to Question 3
sisters = ("Sushmitha", "Hitha", "Jyothsna", "Pavana")
brothers = ("Hariprasad", "Sachin", "Akhil", "Rakesh")
siblings = sisters+brothers
print(siblings)
print("Total number of siblings", len(siblings))
y = list(siblings)
y[1] = "Padmanabha"
y[2] = "Padmavathi"
family_members = tuple(y)
print("Family members are - ",family_members)