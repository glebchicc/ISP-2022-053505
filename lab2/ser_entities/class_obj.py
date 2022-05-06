class Student:

    def __init__(self, avg_score=8.0, name="Kirill") -> None:
        self.avg_score = avg_score
        self.name = name

        avg_score: float
        name: str

        def dismiss():
            print("Oh, you are not a student anymore :(")

        def get_avg_score():
            return self.avg_score

        def get_name():
            return self.name


student_object = Student()


