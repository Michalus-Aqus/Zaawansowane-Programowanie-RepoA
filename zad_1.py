class Student:
    def __init__(self, name, marks):
        self.name: str = name
        self.marks: list = marks

    def is_passed(self):
        # return float(sum(self.marks))/float(len(self.marks))>50
        # not needed to convert to float this conversion happens automatically
        # Moreover one can  use integer // to achive correct result in this case
        return sum(self.marks) / len(self.marks) > 50


def main():
    students = []
    students += [Student("Rupert", [10, 90, 30, 70])]
    students += [Student("John", [10, 90, 30, 71])]

    for s in students:
        print(s.name, " ", s.is_passed())


if __name__ == "__main__":
    main()
