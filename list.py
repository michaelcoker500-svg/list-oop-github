

# Example 1: Create a simple list
Students = ["Michael", "Prince", "Clara"]
print("students list:", Students)

# Example 2: Access items by index
print(f"My bestfriend is: {Students[0]}")
print(f"My brothers name is: {Students[1]}")
print(f"My sisters name is: {Students[2]}")

# How to get the list index using the element name
index_of_prince = Students.index("Prince")
print(f"Index of Prince: {index_of_prince}")
index_of_clara = Students.index("Clara")
print(f"Index of Clara: {index_of_clara}")

# Example 3: Add an item to the list
Students.append("Emma")
print("After adding Emma:", Students)
Students.append("John")
print("After adding John:", Students)

#Adding using the index 
Students.insert(2, "Sonnette")
print(f"After adding sonnette to index 2: {Students}")

# Example 4: Remove an item from the list
Students.remove("Prince")
print("After removing Prince:", Students)

# extending the list
fruits = ["Apple", "Banana", "Cherry"]
Students.extend(["Apple", "Banana", "Cherry"])
print(f"After extending the list: {Students}")

#removing using the index
del fruits[1]
print(f"After removing item at index 1: {fruits}")


# Example 5: Find the length of the list
print("Number of students:", len(Students))

# Example 6: Loop through each item
print("My students:")
for student in Students:
    print("-", student)


#list inside a list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
print(f"The nested list {nested_list}")

#acessing the nested list using the index
print(f"Element at row 1, column 2: {nested_list[1][2]}")


# Example 7: A list with numbers
scores = [10, 20, 30, 40]
print("Scores:", scores)
print("First score:", scores[0])
print("Second score:", scores[1])
print("Third score:", scores[2])
print("Fourth score:", scores[3])
print("Total scores:", len(scores))

# Example 8: A list of mixed data
person = ["Alice", 18, "student"]
print("Person info:", person)

# Example 9: A small real-life list
shopping_list = ["milk", "bread", "eggs"]
print("Shopping list before:", shopping_list)
shopping_list.append("butter")
print("Shopping list after:", shopping_list)

# Example 10: Using a list in a real task
# You can store tasks and mark them complete later.
tasks = ["read", "study", "practice"]
print("Tasks:", tasks)
print("Task 1:", tasks[0])


