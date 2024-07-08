class Student:
    def __init__(self, name, stream, year, roll):
        self.name = name
        self.stream = stream
        self.year = year
        self.roll = roll

    def display(self):
        print(f"\nName of the student : {self.name}")
        print(f"Stream of the student : {self.stream}")
        print(f"Year of the student : {self.year}")
        print(f"Roll number of the student : {self.roll}")


Name = input("\nInput name of the student : ")
Stream = input("Input the stream of the student : ")
Year = input("Input the year of the student : ")
Roll = int(input("Input the roll number of the student : "))

student1 = Student(Name, Stream, Year, Roll)
student1.display()
