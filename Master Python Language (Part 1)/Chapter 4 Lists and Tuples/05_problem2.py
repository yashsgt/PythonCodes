# WAP to accept marks of 6 students and display in a sorted manner?

marks = []

m1 = int(input("Enter students1 marks : "))
marks.append(m1)
m2 = int(input("Enter students2 marks : "))
marks.append(m2)
m3 = int(input("Enter students3 marks : "))
marks.append(m3)
m4 = int(input("Enter students4 marks : "))
marks.append(m4)
m5 = int(input("Enter students5 marks : "))
marks.append(m5)
m6 = int(input("Enter students6 marks : "))
marks.append(m6)
marks.sort()   # To arrange in ascending order.....


print(marks)