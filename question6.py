# Code related to Question 6
MyString = "I am a teacher and I love to inspire and teach people"
# Dividing the string using split function
String_List = MyString.split(' ')
# Converting the list to set
String_Set = set(String_List)

print("total number of unique words in the sentence is ", len(String_Set))
