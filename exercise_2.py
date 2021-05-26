# insert name and surname

name = input("Please enter name: ")
surname = input("Please enter surname: ")

# insert 3 test scores

test1 = input("insert test1 score: ")
test2 = input("insert test2 score: ")
test3 = input("insert test3 score: ")
average = (float(test1) + float(test2) + float(test3)) // 3

def calculate_average():
    average = (float(test1) + float(test2) + float(test3)) // 3
    if average >= 50:
        return "Pass"
    elif average < 50:
        return "fail"


print(name)
print(surname)
print(average)
print(calculate_average())

