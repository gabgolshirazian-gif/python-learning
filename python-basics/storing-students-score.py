person_dic = {}
n = int(input("Enter the number of students:"))
course_list = ["math" , "chemistry" , "physics"]

for i in range(n):
    name = input("name: ")
    source_dic ={}
    for course in course_list:
        score = float(input(f"score {course}:"))
        source_dic[course] = score

    person_dic[name] = source_dic


print(person_dic)