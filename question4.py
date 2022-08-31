# Code related to Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Lenth of set it_companies is : ", len(it_companies))
# adding Twitter to the set it_companies
it_companies.add("Twitter")
# adding 2 IT companies to the set it_companies
it_companies.update({"IBM","Infosys"})
print(it_companies)
# Removing an element from set it_companies
it_companies.remove("IBM")
it_companies.discard("IBM")

print("Set after removing an element ",it_companies)
#What is the diffrence between remove and discard ?
#Answ-> remove() throws exception if the given element is not present in the set.
# However, discard() will not throw any error if the element is not present in the list

# Join A and B
print("A join B is", A.union(B))
# A intersection B
print("A intersection B is", A.intersection(B))

# A subset B?
print("A subset of B? ", A.issubset(B))
#Are A and B disjoint set?
print("A disjoin B? ", A.isdisjoint(B))

#Join A with B and B with A
print("A join B is", A.union(B))
print("B join A is", B.union(A))

#symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)

# Deleting sets it_companies, A, B
it_companies.clear();
A.clear();
B.clear();
#Converting the ages to a set and comparing the length of the list and the set
age_set = set(age)
print("length of set and list", len(age_set)," & ", len(age), " respectively")





