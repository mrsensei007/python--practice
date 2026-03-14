# 1. Dictionary Example
student = {"name": "Amit",
    "age": 22,
    "course": "AI and Data Science",
    "city": "Mumbai"}

print("Student Dictionary:", student)
print("Student Name:", student["name"])

# 2.Dictionary Methods

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student["college"] = "Jio Institute"
print("After Adding College:", student)   # college added

student["age"] = 23
print("Updated Age:", student) # update

removed_value = student.pop("city")
print("Removed city:", removed_value) #removed

print("Dictionary After Pop:", student)

# 3. Decision Making ( if - else )

marks = input("Enter your marks: ")

marks = int(marks)

if marks >= 85:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

##4. for Loops with Dictionary

student = {"name": "Amit",
    "age": 22,
    "course": "AI and Data Science",
    "city": "Mumbai"}

for key, value in student.items():
    print(key, ":", value)

  ###5, type casting exaple 
age_string = "25"
print("Before Type Casting:", type(age_string))

age_integer = int(age_string)
print("After Type Casting:", type(age_integer))

number = 10
number_string = str(number)

print("Integer to String:", number_string, type(number_string))


