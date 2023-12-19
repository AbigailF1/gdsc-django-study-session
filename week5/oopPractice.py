class User:
    def __init__(self, name) -> None:
        self.name = name

class Student(User):
    def __init__(self, name, age, grade) -> None:
        super().__init__(name)
        self.age = age
        self.grade = grade
        self.courses = []

    def display(self):
        course_info = ", ".join([str(course) for course in self.courses])
        return f'Name - {self.name}, Age - {self.age}, Grade - {self.grade}, Courses - {course_info}'

    def addCourse(self, course):
        if course.teacher.subject == course.course_name:
            self.courses.append(course)
        else:
            print(f"Error: The teacher, {course.teacher.name}'s subject ({course.teacher.subject}) does not match the course name ({course.course_name}).")

class Course:
    def __init__(self, course_name, course_id, teacher) -> None:
        self.course_name = course_name
        self.course_id = course_id
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'{self.course_name}: {self.course_id} by {self.teacher}'

class Teacher(User):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

    def __repr__(self):
        return f'{self.name} who teaches {self.subject}'

aman = Teacher('Aman', 'Math')
melaku = Teacher('Melaku', 'CompArch')
selam = Teacher('Selam', 'English')

math = Course("Math", "M1001", melaku)
comparch = Course("CompArch", "C1001", melaku)
english = Course("English", "E1001", selam)

abel = Student('Abel', "21", "3.9")

abel.addCourse(math)
abel.addCourse(comparch)
abel.addCourse(english)

print(abel.display())
