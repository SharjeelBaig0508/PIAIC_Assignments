# Made by SharjeelBaig0508
# A Marksheet Program

print("+" + "-" * 71 + "+")
print("|\t\t\t\tMark Sheet Program\t\t\t|")
print("+" + "-" * 71 + "+")

student_name = input("Enter Student's name >>> ")
print()

student_father = input("Enter Student's Father's name >>> ")
print()

print("+" + "-" * 71 +"+")
total_marks = 550

subject_total_marks = { 
	"English Compulsory" : 75, 
	"Urdu Compulsory" : 75, 
	"Mathematics Comp." : 75, 
	"Physics Inter XI" : 75, 
	"Chemistry Inter XI" : 75, 
	"Computer Science" : 75, 
	"Pakistan Studies" : 50, 
	"Islamiat Studies" : 50 
}

subject_obtained_marks = []

def set_subject_marks(subject, max_marks):
	marks = int(input("Enter Obtained Marks for " + subject + " (0 - " + str(max_marks) + ") >>> "))
	if marks <= max_marks:
		subject_obtained_marks.append(marks)
	else:
		subject_obtained_marks.append(max_marks)

for subject, marks in subject_total_marks.items():
	set_subject_marks(subject, marks)
	print()

obtained_marks = sum(subject_obtained_marks)

def grader(perc):
	if perc <= 100 and perc >= 90:
		return "A+"
	elif perc < 90 and perc >= 80:
		return "A"
	elif perc < 80 and perc >= 70:
		return "B"
	elif perc < 70 and perc >= 60:
		return "C"
	elif perc < 60 and perc >= 50:
		return "D"
	elif perc < 50 and perc >= 40:
		return "E"
	else:
		return "F"

print("+" + "-" * 71 + "+")

print("Student Name :", student_name)

print("Father Name :", student_father)

print("+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+")

print("|Subject\t\t|Obtained Marks\t|Total Marks\t|Grade\t\t|")

print("+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+")

index = 0

for subject, marks in subject_total_marks.items():
	percent = (subject_obtained_marks[index] / marks) * 100
	print("|" + subject, subject_obtained_marks[index], marks, grader(percent), sep = "\t|\t", end = "\t|\n")
	index += 1

print("+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+")

percentage = (obtained_marks / total_marks) * 100

print("|Total :\t", obtained_marks, total_marks, grader(percentage), sep = "\t|\t", end = "\t|\n")

print("+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+")

if percentage >= 40:
	print("Student Passed with", round(percentage, 2),"%")
else:
	print("Student Failed with", round(percentage, 2), "%")

print("Grade :", grader(percentage))

print("+" + "-" * 71 + "+")

