class Student():

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is: ",int(sum/3))


s1 = Student("Rahul" , [12,15,16])
s1.avg_marks()


s1.name ="Tony"
s1.avg_marks()