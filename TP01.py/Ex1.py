# Problem 1 (Easy) · Student profile card

name = "Panhavath"
age = 20
major = "Data Science"
gpa = 3.99
is_scholar = True

print("=" * 30)
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Major   : {major}")
print(f"GPA     : {gpa:.2f}")
print(f"Scholar : {is_scholar}")
print("=" * 30)
for value in (name, age, major, gpa, is_scholar):
    print(repr(value), "->", type(value).__name__)